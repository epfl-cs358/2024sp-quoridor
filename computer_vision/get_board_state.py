import cv2
from PIL import Image
import numpy as np
from .create_grid import *
import os

from .pieces_detection import *

IMAGE_SIZE = 500
SIDE_LENGTH = 9
CELL_SIZE = 24
WALL_SIZE = 6
IMAGE_SIZE = 600


color1 = [140,88,46] #BGR
color2 = [85,65,173] #BGR

def detect_pieces():

    player1 = None # Tuple with (x, y) coordinates 
    player2 = None # Tuple with (x, y) coordinates 
    walls_1 = [] # List of tuples with ((x, y), orientation) (orientation = H or V) 
    walls_2 = [] # List of tuples with ((x, y), orientation) 

    cap = cv2.VideoCapture(0)

    # Set capture format to 'MJPG'
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('m', 'j', 'p', 'g'))

    while player1 == None or player2 == None:

        ret = False
        while not ret:
            ret, frame = cap.read()
    
        # USED WHEN DEBUGGING WHILE NOT AT DLL with picture of the board stored
        """ script_dir = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(script_dir, "image.png")
        frame = cv2.imread(image_dir, cv2.IMREAD_COLOR) """

        warped_img, intersections = game_board(frame.copy(),IMAGE_SIZE, SIDE_LENGTH, CELL_SIZE, WALL_SIZE)
        
        frame_walls1, walls_1 = detect_walls(color1, warped_img.copy(), intersections)
        frame_walls2, walls_2 = detect_walls(color2, warped_img.copy(), intersections)
        frame_piece1, player1 = detect_player(color1, warped_img.copy(), intersections)
        frame_piece2, player2 = detect_player(color2, warped_img.copy(), intersections)

        walls = walls_1 + walls_2

        print(f'Found {len(walls)} walls')

        # ---- FOR DEBUG AND VIZUALISATION PURPOSES --------
        """ while True: 
            cv2.imshow('frame', frame_piece1)
            cv2.imshow('frame', frame_piece2)
            cv2.imshow('frame', frame_walls1)
            cv2.imshow('frame', frame_walls2)

            cv2.waitKey(0)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break """

    # cv2.destroyAllWindows()

    print(player1)
    print(player2)

    return player1, player2, walls

if __name__ == "__main__":
    p1, p2, w = detect_pieces()
    print(p1)
    print(p2)
    print(w)
import cv2
from PIL import Image
import numpy as np
import create_grid as grid

import pieces_detection as detect

SIDE_LENGTH = 9
CELL_SIZE = 24
WALL_SIZE = 6
IMAGE_SIZE = 600


color1 = [127,47,26]
color2 = [0,0,255] 

def detect_pieces():

    player1 = None # Tuple with (x, y) coordinates 
    player2 = None # Tuple with (x, y) coordinates 
    walls_1 = [] # List of tuples with ((x, y), orientation) (orientation = H or V) 
    walls_2 = [] # List of tuples with ((x, y), orientation) 

    cap = cv2.VideoCapture(0)

    # Set capture format to 'MJPG'
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('m', 'j', 'p', 'g'))

    while player1 == None or player2 == None or walls_1 == [] or walls_2 == []:

        ret = False
        while not ret:
            ret, frame = cap.read()
    
        # USED WHEN DEBUGGING WHILE NOT AT DLL with picture of the board stored
        # frame = cv2.imread("image.png", cv2.IMREAD_COLOR)

        warped_img, intersections = grid.game_board(frame.copy(),IMAGE_SIZE, SIDE_LENGTH, CELL_SIZE, WALL_SIZE)
        
        frame_walls1, walls_1 = detect.detect_walls(color1, warped_img.copy(), intersections)
        frame_walls2, walls_2 = detect.detect_walls(color2, warped_img.copy(), intersections)
        frame_piece1, player1 = detect.detect_player(color1, warped_img.copy(), intersections)
        frame_piece2, player2 = detect.detect_player(color2, warped_img.copy(), intersections)

        walls = walls_1 + walls_2

        print(f'Found {len(walls)} walls')

        # ---- FOR DEBUG AND VIZUALISATION PURPOSES --------
        # while True: 
        #     # cv2.imshow('frame', frame_piece1)
        #     # cv2.imshow('frame', frame_piece2)
        #     # cv2.imshow('frame', frame_walls1)
        #     # cv2.imshow('frame', frame_walls2)

        #     # cv2.waitKey(0)

        #     if cv2.waitKey(1) & 0xFF == ord('q'):
        #         break

    # cv2.destroyAllWindows()

    return player1, player2, walls

if __name__ == "__main__":
    p1, p2, w = detect_pieces()
    print(p1)
    print(p2)
    print(w)
import cv2
import numpy as np

from util import get_limits

SIDE_LENGTH = 8
CELL_SIZE = 24
WALL_SIZE = 6

color = [99, 56, 44]  # Color in BGR colorspace

color_wall1 = []
color_wall2 = []
color_player1 = []
color_player2 = []

def detect_color(color, frame):
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(color=color, sensitivity=30)
    return cv2.inRange(hsvImage, lowerLimit, upperLimit)


def detect_walls(color, image, intersections):
    #Create color mask
    mask = detect_color(color, image)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(f'Found {len(contours)} contours')
    walls = []

    for cnt in contours:
        area = cv2.contourArea(cnt)

        # Ignore contours that are too small or too large

        #TODO: Tune these values
        if area < 3700 or 100000 < area:
            continue

        # cv.minAreaRect returns:
        # (center(x, y), (width, height), angle of rotation) = cv2.minAreaRect(c)
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        center = (int(rect[0][0]),int(rect[0][1])) 
        angle = int(rect[2])

        #Detect cell of the wall
        cell = detect_cell_wall(center, intersections)

        walls.append((cell,angle))
        # Draw each contour only for visualisation purposes
        image = cv2.drawContours(image,[box],0,color,2)
        image = cv2.putText(image, f"({cell[0]}, {cell[1]})", (center[0], center[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    return image, walls

def detect_player(color, image, intersections):
    #Create color mask
    mask = detect_color(color, image)
    
    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(f'Found {len(contours)} contours')
    player = [0,0,0]

    for cnt in contours:
        area = cv2.contourArea(cnt)
        # (center(x, y), (width, height), angle of rotation) = cv2.minAreaRect(c)
        rect = cv2.minAreaRect(cnt)
        center = (int(rect[0][0]),int(rect[0][1])) 

        #Keep the larger area only 
        if (area > player[1]) :
            player = [center, area, rect]

    # Now detect the cell associated with this player

    cell = detect_cell_player(player[0], intersections)
        
    # Draw each contour only for visualisation purposes
    box = cv2.boxPoints(player[2])
    box = np.int0(box)
    image = cv2.drawContours(image,[box],0,color,2)
    image = cv2.putText(image, f"({cell[0]}, {cell[1]})", (player[0][0], player[0][1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)


    return image, cell



def detect_cell_player(center, intersections):
    cx = center[0]
    cy = center[1]

    for i in range(0, len(intersections)-SIDE_LENGTH*2-1):
        print("index is ", i)
        top_left = intersections[i+0]
        top_right = intersections[i+1]
        bottom_left = intersections[i+SIDE_LENGTH*2]
        bottom_right = intersections[i+1+SIDE_LENGTH*2]
        print("corners are: ", top_left[0], " ", top_left[1], ", ",  top_right[0], " ", top_right[1], ", ", bottom_left[0], " ", bottom_left[1], ", ", bottom_right[0], " ", bottom_right[1])
        print (" and object center is ", cx, " ", cy)
        if top_left[0] <= cx and top_left[1] >= cy and top_right[0] >= cx and top_right[1] >= cy and bottom_left[0] <= cx and bottom_left[1] <= cy and bottom_right[0] >= cx and bottom_right[1] <= cy:
            print("x marks the spot")
            return top_left[2],top_left[3]


def detect_cell_wall(center, intersections):
    return NotImplemented #TODO: Implement
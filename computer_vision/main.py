import cv2
from PIL import Image
import numpy as np
import create_grid as grid

from util import get_limits

SIDE_LENGTH = 8
CELL_SIZE = 24
WALL_SIZE = 6

color = [99, 56, 44]  # Color in BGR colorspace

cap = cv2.VideoCapture(0)
# Set capture format to 'MJPG'
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('m', 'j', 'p', 'g'))

while True:
    ret, frame = cap.read()
    if not ret:
        break


    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(color=color, sensitivity=30)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    mask_ = Image.fromarray(mask)

    # Optional: Apply morphological operations to clean up the mask
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Find the aruco markers and build the grid
    detected_markers, intersections = grid.game_board(frame, SIDE_LENGTH, CELL_SIZE, WALL_SIZE)

    if len(intersections) >= 1:
        print('------------------')
        print(intersections[0])

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(f'Found {len(contours)} contours')
    final_pieces = []
    # Draw bounding box for each contour
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        if w < 30 or h < 30:
            continue

        # Add the contour to the final pieces list
        final_pieces.append(cnt)

        print(f'x: {x}, y: {y}, w: {w}, h: {h}')
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)


    # Now I need to find to which grid the detected contours belong to based on the aruco markers detector
    for cnt in final_pieces:
        M = cv2.moments(cnt)
        
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])

            cell = None

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
                    cell = top_left[2],top_left[3]

            if cell is not None:               
                print(f"Contour centroid belongs to cell ({cell[0]}, {cell[1]})")
            
                # Display the grid of the centroid on the frame
                cv2.putText(frame, f"({cell[0]}, {cell[1]})", (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                
                # Optional: Draw centroid on the frame
                cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

    cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)  # Optionally display the mask

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# def detect_cell(cx, cy, intersections):

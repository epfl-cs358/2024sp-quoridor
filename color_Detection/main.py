import cv2
from PIL import Image
import numpy as np

from util import get_limits

color = [99, 56, 44]  # Color in BGR colorspace

cap = cv2.VideoCapture(1)
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

    # Now I need to find to which grid the detected contours belong to
    # I will use the center of the bounding box to determine this
    # I will divide the frame into 8x8 grid

    for i in range(8):
        for j in range(8):
            cv2.rectangle(frame, (i * 100, j * 100), (i * 100 + 100, j * 100 + 100), (255, 0, 0), 2)

    for cnt in final_pieces:
        M = cv2.moments(cnt)
        
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            grid_x = cx // 100
            grid_y = cy // 100

            
            print(f"Contour centroid belongs to grid ({grid_x}, {grid_y})")

            # Display the grid of the centroid on the frame
            cv2.putText(frame, f"({grid_x}, {grid_y})", (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            # Optional: Draw centroid on the frame
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

    cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)  # Optionally display the mask

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

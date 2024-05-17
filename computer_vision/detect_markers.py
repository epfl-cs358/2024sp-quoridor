import numpy as np
import cv2
from cv2 import aruco
from time import sleep
from collections import defaultdict


## takes coordinates of two perpendicular lines and compute the intersection
## returns the coordinates of the intersection
def compute_intersection(line1, line2):
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]

    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denominator == 0:
        return None
    
    intersection_x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denominator
    intersection_y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denominator
    
    return int(intersection_x), int(intersection_y)

## computes the elements to be displayed and display them
## arguments are the four corners of each marker, their IDs and the current frame (image)
def aruco_display(corners, ids, rejected, image, side_length):

    ## create the variable to store all the intersections coordinates
    intersections = []

    if len(corners) > 0:
        ids = ids.flatten()

        ## centersIDs contains a dictionary entry for each identical marker and two values attributed to each entry (one for each duplicate of the marker)
        ## those values represent the corners of those duplicate markers that should be linked to create a grid line
        centersIDs = {}
        vertical_lines = []
        horizontal_lines = []

        ## for each marker
        for (markerCorner, markerID) in zip(corners, ids):
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners
 
            ## reformat the coordinates of the 4 corners
            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))
 
            ## draw between the corners to frame the marker
            cv2.line(image, topLeft, topRight, (255, 0, 0), 2)
            cv2.line(image, topRight, bottomRight, (0, 255, 0), 2)
            cv2.line(image, bottomRight, bottomLeft, (255, 0, 0), 2)
            cv2.line(image, bottomLeft, topLeft, (0, 255, 0), 2)
 
 
            ## display the marker id
            cv2.putText(image, str(markerID), (topLeft[0], topLeft[1] - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 2)

            ## populates the centersIDs variable
            if markerID in centersIDs:
                ## when the marker belongs to a row, link top and bottom
                if markerID < side_length :
                    centersIDs[markerID].append((bottomRight, topRight))
                ## else link left and right
                else :
                    centersIDs[markerID].append((bottomLeft, bottomRight))
            else:
                if markerID < side_length:
                    centersIDs[markerID] = [(bottomRight, topRight)]
                else:
                    centersIDs[markerID] = [(bottomLeft, bottomRight)]

        ## takes the values from centersIDs and draw the lines that make up the grid
        for markerID, centers in centersIDs.items():
            if len(centers) == 2:
                line1 = (centers[0][0], centers[1][0])
                line2 = (centers[0][1], centers[1][1])
                cv2.line(image, line1[0], line1[1], (0, 0, 255), 2)
                cv2.line(image, line2[0], line2[1], (0, 0, 255), 2)
                ## each line is added in either the list of horizontal or vertical lines
                if (markerID < side_length):
                    horizontal_lines.append((line1, markerID))
                    horizontal_lines.append((line2, markerID))
                else:
                    vertical_lines.append((line1, int(markerID)-side_length))
                    vertical_lines.append((line2, int(markerID)-side_length))

        ## if at least two perpendicular lines have been drawn, compute their intersection                
        if (len(horizontal_lines) >= 1 and len(vertical_lines) >= 1):
            for h_line in horizontal_lines:
                for v_line in vertical_lines:
                    x, y = compute_intersection(h_line[0], v_line[0])
                    cv2.circle(image, (x, y), 5, (255, 255, 0), -1)
                    ## add the computed intersection in the array to be returned
                    intersections.append((x,y, v_line[1], h_line[1]))
                    some = markerID
                    
    ## return the frame with newly displayed information and the array of intersection coordinates
    return image, intersections

def detect_markers(frame, side_length):
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_100)
    aruco_param = aruco.DetectorParameters()
    detector = aruco.ArucoDetector(aruco_dict, aruco_param)

    (corners, ids, rejected) = detector.detectMarkers(frame)
    detected_markers, intersections = aruco_display(corners, ids, rejected, frame, side_length)
    return detected_markers, intersections

def show_camera(index):
    cap = cv2.VideoCapture(index)
	# Set capture format to 'MJPG'
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('m','j','p','g'))
    while True:
        ret, frame = cap.read()
        if not ret:
            print(f"Camera {index} is not available")
            print(ret)
            break

        aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_100)
        aruco_param = aruco.DetectorParameters()
        detector = aruco.ArucoDetector(aruco_dict, aruco_param)

        (corners, ids, rejected) = detector.detectMarkers(frame)
        detected_markers, intersections = aruco_display(corners, ids, rejected, frame, 3)

        cv2.imshow("Camera", detected_markers)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()



def main():
    
    while True:
        show_camera(1)
        sleep(1)

if __name__ == "__main__":
    main()
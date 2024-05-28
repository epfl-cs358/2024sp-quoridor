import numpy as np
import math
import cv2
from cv2 import aruco
from collections import defaultdict
from time import sleep

IMAGE_SIZE = 500
SIDE_LENGTH = 9
CELL_SIZE = 24
WALL_SIZE = 6

def compute_direction(point1, point2):
    vector = np.array(point1, dtype = float) - np.array(point2, dtype=float)
    length = np.linalg.norm(vector)
    print("vector is", vector)
    print("length is", length)
    vector /= length
    return vector, length

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
    
    return (int(intersection_x), int(intersection_y))

def correct_perspective(image, image_size):
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    aruco_param = aruco.DetectorParameters()
    detector = aruco.ArucoDetector(aruco_dict, aruco_param)

    (corners, ids, rejected) = detector.detectMarkers(image)

    src_corners = np.zeros((4,2), dtype=np.float32)
    inner_corners = np.zeros((4,2), dtype=np.float32)
    dst_corners = np.array([
        [0.0, 0.0],
        [image_size, 0.0], 
        [image_size, image_size], 
        [0.0, image_size]
    ], dtype=np.float32)

    if len(corners) == 4:
        ids = ids.flatten()

        for (markerCorner, markerID) in zip(corners, ids):
            marker_corners = markerCorner.reshape((4,2))
            src_corners[markerID] = marker_corners[markerID]
            inner_coordinate = (markerID + 2) % 4
            inner_corners[markerID] = marker_corners[inner_coordinate]

        M = cv2.getPerspectiveTransform(src_corners, dst_corners)
        dst = cv2.warpPerspective(image, M, (image_size, image_size))

        ones = np.ones((4, 1))
        inner_corners_homogeneous = np.hstack([inner_corners, ones])
        transformed_inner_corners_homogeneous = M @ inner_corners_homogeneous.T
        transformed_inner_corners = transformed_inner_corners_homogeneous[:2, :] / transformed_inner_corners_homogeneous[2, :]
        transformed_inner_corners = transformed_inner_corners.T

        return dst, transformed_inner_corners, ids
    return image, None, None



def aruco_detect(image, corners, ids):
    board_corners = {}

    if corners is not None and ids is not None and len(corners) > 0:

        for (markerCorner, markerID) in zip(corners, ids):
            (topLeft, topRight, bottomRight, bottomLeft) = corners

            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))

            cv2.line(image, topLeft, topRight, (255, 0, 0), 2)
            cv2.line(image, topRight, bottomRight, (0, 255, 0), 2)
            cv2.line(image, bottomRight, bottomLeft, (255, 0, 0), 2)
            cv2.line(image, bottomLeft, topLeft, (0, 255, 0), 2)

            ##cv2.putText(image, str(markerID), (topLeft[0], topLeft[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            if markerID == 0:
                board_corners["top left"] = bottomLeft
            elif markerID == 1:
                board_corners["top right"] = bottomRight
            elif markerID == 2:
                board_corners["bottom right"] = topRight
            elif markerID == 3:
                board_corners["bottom left"] = topLeft
                
    return image, board_corners

def create_grid(image, board_corners, side_length, cell_size, wall_size):
    intersections = []
    vertical_lines = []
    ratio = cell_size//wall_size
    number_units = (ratio * side_length) + side_length -1
    number_grid_lines = side_length*2

    if len(board_corners) == 4:
        borders = {}

        ## create the four lines that delimit the board. Also, for each line, compute length, direction and give it its appropriate coordinate
        borders["top"] = (compute_direction(board_corners["top right"], board_corners["top left"]), SIDE_LENGTH-1)
        borders["right"] = (compute_direction(board_corners["top right"], board_corners["bottom right"]), SIDE_LENGTH-1)
        borders["bottom"] = (compute_direction(board_corners["bottom right"], board_corners["bottom left"]), 0)
        borders["left"] = (compute_direction(board_corners["top left"], board_corners["bottom left"]), 0)


        for region, border in borders.items():
            unit_distance = border[0][1] / number_units
            starting_point = None
            direction = None
            if region == "top":
                starting_point = board_corners["top left"]
                direction = "horizontal"
            elif region == "bottom":
                starting_point = board_corners["bottom left"]
                direction = "horizontal"
            elif region == "left":
                starting_point = board_corners["bottom left"]
                direction = "vertical"
            elif region == "right":
                starting_point = board_corners["bottom right"]
                direction = "vertical"

            if starting_point is not None:
                for i in range(number_units+1):
                   check_index = i % (ratio+1)
                   if check_index == 0 or check_index == ratio:
                        newPoint = starting_point + border[0][0] * (unit_distance * i)
                        newPoint = (int(newPoint[0]), int(newPoint[1]))
                        coordinate = math.floor(i/(ratio+1))
                        if direction == "horizontal":
                           intersections.append((newPoint, (border[1], coordinate)))
                        else:
                           intersections.append((newPoint, (coordinate, border[1])))
                        ##cv2.circle(image, (newPoint), 5, (255, 255, 0), -1)
                        ##cv2.putText(image, str(coordinate), (newPoint), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    if len(intersections) > 0:
        for x in range(number_grid_lines):
            start_point = intersections[x][0]
            end_point = intersections[x + 2*number_grid_lines][0]
            cv2.line(image, start_point, end_point, (0, 0, 255), 2)
            coordinate = intersections[x][1][0]
            vertical_lines.append(((start_point, end_point), coordinate))

        for y in range(number_grid_lines):
            start_point = intersections[y + 3*number_grid_lines][0]
            end_point = intersections[y + number_grid_lines][0]
            line1 = (start_point, end_point)
            cv2.line(image, start_point, end_point, (0,0,225), 2)
            coordinate = intersections[y + 3*number_grid_lines][1][1]
            for i in range(number_grid_lines):
                line2 = vertical_lines[i]
                intersections.append((compute_intersection(line1, line2[0]), (line2[1], coordinate)))
                            
    return image, intersections
        
def game_board(frame, IMAGE_SIZE, SIDE_LENGTH, CELL_SIZE, WALL_SIZE):
    (image, corners, ids) = correct_perspective(frame, IMAGE_SIZE)
    (image, board_corners) = aruco_detect(image, corners, ids)
    image, intersections = create_grid(image, board_corners, SIDE_LENGTH, CELL_SIZE, WALL_SIZE)
    return image, intersections

def show_camera(index):
    cap = cv2.VideoCapture(index)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('m','j','p','g'))
    while True:
        ret, frame = cap.read()
        if not ret:
            print(f"Camera {index} is not available")
            print(ret)
            break

        image, intersections = game_board(frame, IMAGE_SIZE, SIDE_LENGTH, CELL_SIZE, WALL_SIZE)
        
        cv2.imshow("Camera", image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def main():
    
    while True:
        show_camera(0)
        sleep(1)

if __name__ == "__main__":
    main()


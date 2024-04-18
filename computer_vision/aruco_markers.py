import numpy as np
import cv2, PIL
from cv2 import aruco
import os


def generate_single_marker(aruco_dict):
    marker_size = int(input("Enter the marker size: "))
    marker_id = int(input("Enter the marker ID: "))

    marker_img = aruco.generateImageMarker(aruco_dict, marker_id, marker_size)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(script_dir, "marker_{}.jpg".format(marker_id))

    cv2.imwrite(output_file, marker_img)
    marker_img = cv2.imread(output_file)
    cv2.imshow("Marker", marker_img)

    print("Dimensions: ", marker_img.shape)
    cv2.waitKey(0)

def generate_bulk_markers(aruco_dict):
    marker_size = int(input("Enter the marker size: "))
    num_markers = int(input("Enter the number of markers to generate: "))
    marker_imgs = []
    script_dir = os.path.dirname(os.path.abspath(__file__))

    for marker_id in range(num_markers):
        marker_img = aruco.generateImageMarker(aruco_dict, marker_id, marker_size)
        output_file = os.path.join(script_dir, "marker_{}.jpg".format(marker_id))
        cv2.imwrite(output_file, marker_img)
        marker_imgs.append(cv2.imread(output_file))

    for marker_img in marker_imgs:
        cv2.imshow("Marker", marker_img)
        print("Dimensions: ", marker_img.shape)
        cv2.waitKey(0)


def main():
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

    
    user_input = input("Press 1 to generate a single marker. Press 2 to generate markers in bulk: ")
    print(user_input)

    if (user_input == "1"):
        generate_single_marker(aruco_dict)
    elif (user_input == "2"):
        generate_bulk_markers(aruco_dict)
    else:
        print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()

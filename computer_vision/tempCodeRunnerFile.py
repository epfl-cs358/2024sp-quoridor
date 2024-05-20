    for x in range(number_grid_lines):
            start_point = intersections[x][0]
            end_point = intersections[x + 2*number_grid_lines][0]
            cv2.line(image, start_point, end_point, (0, 0, 255), 2)
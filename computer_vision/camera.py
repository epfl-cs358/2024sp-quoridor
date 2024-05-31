from time import sleep
import cv2

# fetches the camera feed.
# arg index : which camera to take the feed from. Most commonly, index 0 is the computer's integrated camera, index 1 for a plugged-in camera
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
        cv2.imshow("Camera", frame)
        print(f"Camera {index} is available")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


while True:
    show_camera(1)
    sleep(1)
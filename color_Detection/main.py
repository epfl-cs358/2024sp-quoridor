import cv2
from PIL import Image

from util import get_limits


color = [99, 56, 44]  # color in BGR colorspace
# cap = cv2.VideoCapture(0)

cap = cv2.VideoCapture(1)
# Set capture format to 'MJPG'
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('m','j','p','g'))
while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=color)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    # mask = cv2.inRange(frame,color,color)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()


import cv2
import numpy as np

def apply_mask(image, mask):
    lower, upper = mask
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array(lower)
    upper = np.array(upper)
    return cv2.bitwise_and(image, image, mask=cv2.inRange(hsv, lower, upper))

video = cv2.VideoCapture('3.mp4')

cv2.namedWindow("bosch", cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame', 600, 600)
mask_range = [30, 30, 100, 80, 255, 255]

def event_listener(index):
    def set_value(val):
        global mask_range
        mask_range[index] = val
    return set_value

for i in range(6):
    cv2.createTrackbar(str(i), 'bosch', mask_range[i], 255, event_listener(i))

while(video.isOpened()):
    ret, frame = video.read()
    if not ret:
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    mask = (mask_range[0:3], mask_range[3:7])
    img = apply_mask(frame, mask)

    cv2.imshow('bosch', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

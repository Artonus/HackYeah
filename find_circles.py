import cv2
import imutils
import statistics
import numpy as np


def apply_mask(image, mask):
    lower, upper = mask
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array(lower)
    upper = np.array(upper)
    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)

    return output


RED_MASK = ([150, 150, 0], [180, 255, 255])
BLUE_MASK = ([0, 150, 150], [255, 255, 180])
GREEN_MASK = ([30, 30, 100], [80, 255, 255])

video = cv2.VideoCapture('3.mp4')

cv2.namedWindow("bosch", cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame', 600, 600)


def mean1D(array):
    x_sum = 0
    y_sum = 0
    count = len(array)
    for a in array:
        x, y = a[0]
        x_sum += x
        y_sum += y
    return (int(x_sum / count), int(y_sum / count))


def or_images(images):
    target = images.pop()
    for i in images:
        target = cv2.bitwise_or(target, i)
    return target


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

    mask = (mask_range[0:3], mask_range[3:7])
    img = apply_mask(frame, mask)

    cv2.imshow('bosch', img)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)

    cnts = cv2.findContours(
        thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # for c in cnts:
    #     RED = (0, 0, 255)
    #     cv2.circle(gray, mean1D(c), 5, RED, 6)

    cv2.imshow('bosch', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

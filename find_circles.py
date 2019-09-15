import cv2
import imutils
import numpy as np
from algorithms import *
from config import *


def apply_mask(image, mask):
    lower, upper = mask
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array(lower)
    upper = np.array(upper)
    mask = cv2.inRange(hsv, lower, upper)
    return cv2.bitwise_and(image, image, mask=mask)



def mean1D(array):
    x_sum = y_sum = 0
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

def distance_from_x(a):
    def dist(b):
        x = a[0] - b[0]
        y = a[1] - b[1]
        return x * x + y * y
    return dist

def read_point(image, mask, img_center):
    image = apply_mask(image, mask)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)
    cnts = cv2.findContours(
        thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    points = []
    for c in cnts:
        point = mean1D(c)
        points.append(point)
    return min(points, key=distance_from_x(img_center))
    # return points

def run(controller, display=True):

    if display:
        cv2.namedWindow("bosch", cv2.WINDOW_NORMAL)
        cv2.resizeWindow('frame', 600, 600)

    video = cv2.VideoCapture(source)
    ret, frame = video.read()

    TOP_POINT = read_point(frame, TOP_MASK, frame.shape)
    CENTER_POINT = read_point(frame, CENTER_MASK, frame.shape)

    while(video.isOpened()):
        ret, frame = video.read()
        if not ret:
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        img = apply_mask(frame, ROTATING_MASK)

        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)

        thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.erode(thresh, None, iterations=2)
        thresh = cv2.dilate(thresh, None, iterations=2)

        cnts = cv2.findContours(
            thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        points = []
        for c in cnts:
            point = mean1D(c)
            cv2.circle(frame, point, 5, (255,0,0), 6)
            points.append(point)

        ROTATING_POINT = min(points, key=distance_from_x(CENTER_POINT))
        phi = findAlfaOnThreePoints(CENTER_POINT, TOP_POINT, ROTATING_POINT)

        if display:
            x_offset = int(math.cos(phi) * 100)
            y_offset = int(math.sin(phi) * 100)
            RED = (0, 0, 255)
            cv2.circle(frame, ROTATING_POINT, 5, RED, 6)

            cv2.line(frame, ROTATING_POINT, TOP_POINT, RED, 3)
            cv2.line(frame, ROTATING_POINT, CENTER_POINT, RED, 3)
            cv2.line(frame, TOP_POINT, CENTER_POINT, RED, 3)

            cv2.circle(frame, (CENTER_POINT[0] + x_offset,
                               CENTER_POINT[1] + y_offset), 5, (0, 255, 0), 6)
            cv2.imshow('bosch', frame)

        controller(phi)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

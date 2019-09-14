import cv2
import numpy as np
import matplotlib.pyplot as plt

def find_in_range(image, lower, upper):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array(lower)
    upper = np.array(upper)
    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(image, image, mask= mask)

    return np.hstack([image, output])

boundries = [
    ([150, 150, 0], [180, 255, 255]), # red
    # ([0,0,0], [255,255,255]),
    # ([0, 25, 0], [0, 255, 0]),
    # ([50, 5, 20], [140, 110, 110]), # red
    ([0, 150, 150], [255, 255, 180]), # blue
    ([65, 60, 60], [80, 250, 250]),
    ([30, 30, 100], [80, 255, 255])
    ]



video = cv2.VideoCapture('video.mp4')

cv2.namedWindow("bosch", cv2.WINDOW_NORMAL)  
cv2.resizeWindow('frame', 600, 600)


while(video.isOpened()):
    ret, frame = video.read()
    # cv2.imshow('bosch',frame)
    cv2.imshow('bosch', find_in_range(frame, boundries[2][0], boundries[2][1]))
    # plt.imshow(find_in_range(frame, boundries))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

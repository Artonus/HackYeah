import cv2
import numpy as np
import matplotlib.pyplot as plt

def find_in_range(image, boundries):
    for (lower, upper) in boundries:
        # lower = np.array(lower, dtype = "uint8")
        # upper = np.array(upper, dtype = "uint8")
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # find the colors within the specified boundaries and apply
        # the mask
        # mask = cv2.inRange(image, lower, upper)
        lower_red = np.array([30,150,50])
        upper_red = np.array([255,255,180])
    
        mask = cv2.inRange(hsv, lower_red, upper_red)
        output = cv2.bitwise_and(image, image, mask = mask)

        return np.hstack([image, output])

boundries = [
([80, 25, 40], [110, 50, 70]), # red
([60, 100, 30], [110, 160, 80]), # green
([20, 50, 130], [50, 90, 165]), # blue
]


video = cv2.VideoCapture('video.mp4')

cv2.namedWindow("bosch", cv2.WINDOW_NORMAL)  
cv2.resizeWindow('frame', 600, 600)


while(video.isOpened()):
    ret, frame = video.read()
    # cv2.imshow('bosch',frame)
    cv2.imshow('bosch', find_in_range(frame, boundries))
    # plt.imshow(find_in_range(frame, boundries))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

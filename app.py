import cv2 as cv
import numpy as np

image = cv.imread('./rotor.jpg')
grayscale = np.copy(image)
grayscale = cv.cvtColor(grayscale, cv.COLOR_RGB2GRAY)
blur = cv.GaussianBlur(grayscale, (5, 5), 0)
canny = cv.Canny(blur, 30, 150)
cv.imshow('xd', canny)

cv.waitKey(0)
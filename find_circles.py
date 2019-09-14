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


# RED_MASK = ([150, 150, 0], [180, 255, 255])
# BLUE_MASK = ([0, 150, 150], [255, 255, 180])
# GREEN_MASK = ([30, 30, 100], [80, 255, 255])

CENTER_MASK = ([79, 109, 97], [143, 210, 191])
TOP_MASK = ([27, 156, 58], [32, 255, 255])
SPINNING_MASK = ([142, 181, 0], [255, 255, 255])

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

# for i in range(6):
#     cv2.createTrackbar(str(i), 'bosch', mask_range[i], 255, event_listener(i))


def read_point(image, mask):
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
    return points


ret, frame = video.read()
TOP = read_point(frame, TOP_MASK)[0]
CENTER = read_point(frame, CENTER_MASK)[0]

print(TOP)
print(CENTER)

while(video.isOpened()):
    ret, frame = video.read()
    if not ret:
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # mask = (mask_range[0:3], mask_range[3:7])
    # top_img = apply_mask(frame, TOP_MASK)
    # center_img = apply_mask(frame, CENTER_MASK)
    # spinning_img = apply_mask(frame, SPINNING_MASK)

    # img = apply_mask(frame, mask)
    # img = or_images([top_img, center_img, spinning_img])
    img = apply_mask(frame, SPINNING_MASK)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)

    cnts = cv2.findContours(
        thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    ROTATING_POINT = mean1D(cnts[0])
    RED = (0, 0, 255)
    cv2.circle(frame, ROTATING_POINT, 5, RED, 6)
    print(ROTATING_POINT)

    cv2.imshow('bosch', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

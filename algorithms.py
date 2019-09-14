import math
import cv2
import numpy as np


def diff(A, B):
    return (A[0] - B[0], A[1] - B[1])

def findAlfaOnThreePoints(AnchorPoint, pointB, pointC):
    v1 = diff(pointB, AnchorPoint)
    v2 = diff(pointC, AnchorPoint)
    ang = math.atan2(v1[0]*v2[1]-v2[0]*v1[1], v1[0]*v2[0]+v1[1]*v2[1])
    return ang - math.pi / 2

# def getMatrixFrom4Points(point1,point2,point3,point4):
#     pts1 = np.float32([point1,point2,point3,point4])
#     pts2 = np.float32([[300,300],[300,0],[0,300],[300,600]])
#     return cv2.getPerspectiveTransform(pts1,pts2)


# refpointy to stałe punkty, point ma być ściśle zmienny
def what_do(refpoint1, refpoint2, point):
    a = (refpoint2[1] - refpoint1[1]) / (refpoint2[0] - refpoint1[0])
    b = refpoint2[1] - (a * refpoint2[0])
    isRaising = a > 0
    y = (a * point[0]) + b
    return point[1] > y and isRaising
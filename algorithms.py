import math
import cv2
import numpy as np


def findAlfaOnThreePoints(pointA, pointB, pointC):
    R0 = (pointB[0]-pointA[0])*(pointB[0]-pointA[0])+(pointB[1]-pointA[1])*(pointB[1]-pointA[1])
    R1 = (pointC[0]-pointA[0])*(pointC[0]-pointA[0])+(pointC[1]-pointA[1])*(pointC[1]-pointA[1])
    R2 = (pointB[0]-pointC[1])*(pointB[0]-pointC[1])+(pointB[1]-pointC[0])*(pointB[1]-pointC[0])
    cosalfa = (R0 + R1 - R2)/2*math.sqrt(R0*R2)
    return math.acos(cosalfa)

def getMatrixFrom4Points(point1,point2,point3,point4):
    pts1 = np.float32([point1,point2,point3,point4])
    pts2 = np.float32([[300,300],[300,0],[0,300],[300,600]])
    return cv2.getPerspectiveTransform(pts1,pts2)

def what_do(refpoint1,refpoint2,point):         #refpointy to stałe punkty, point ma być ściśle zmienny
    a = ( refpoint2[1] - refpoint1[1] ) / ( refpoint2[0] - refpoint1[0] )
    b = refpoint2[1] - ( a * refpoint2[0] )
    isRaising = a > 0 ? true : false
    y = ( a * point[0] ) + b
    if point[1] > y:
        return true                             #czyli krecimy zgodnie z ruchem wskazówek zegara!
    else
        return false                            #czyli że nie

img = cv2.imread("kolo.png")
rows,cols,ch = img.shape
# dst = cv2.warpAffine(img, getMatrixFrom4Points((830,1359),(1820,203),(1002,1207),(2673,1178)), (img.shape[1], img.shape[0]))
M = getMatrixFrom4Points((830,1359),(1820,203),(1002,1207),(2673,1178));
import math
import cv2
import numpy

def findAlfaOnThreePoints(pointA, pointB, pointC):
    v1 = [pointB[0]-pointA[0], pointB[1]-pointA[1]]
    v2 = [pointC[0]-pointA[0], pointC[1]-pointA[1]]
    # print(v1)
    # print(v2)
    len1 = v1[0]*v1[0]+v1[1]*v1[1]
    # print(len1) 
    len2 = v2[0]*v2[0]+v2[1]*v2[1]
    # print(len2*len2) 
    return math.acos(numpy.dot(v1,v2) / len1*len2)

# def getMatrixFrom4Points(point1,point2,point3,point4):
#     pts1 = np.float32([point1,point2,point3,point4])
#     pts2 = np.float32([[300,300],[300,0],[0,300],[300,600]])
#     return cv2.getPerspectiveTransform(pts1,pts2)


# print(findAlfaOnThreePoints((400,300),(400,0),(100,300)))
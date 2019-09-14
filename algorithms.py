import math
import cv2
import numpy

def findAlfaOnThreePoints(pointA, pointB, pointC):
    v1 = [pointB[0]-pointA[0], pointB[1]-pointA[1]]
    v2 = [pointC[0]-pointA[0], pointC[1]-pointA[1]]
    len1 = math.sqrt(v1[0]*v1[0]+v1[1]*v1[1])
    len2 = math.sqrt(v2[0]*v2[0]+v2[1]*v2[1])
    print(len2*len2)
    print(numpy.dot(v1,v2)) 
    print(numpy.dot(v1,v2)/(len1*len2))
    return math.acos(numpy.dot(v1,v2)/(len1*len2))

# def getMatrixFrom4Points(point1,point2,point3,point4):
#     pts1 = np.float32([point1,point2,point3,point4])
#     pts2 = np.float32([[300,300],[300,0],[0,300],[300,600]])
#     return cv2.getPerspectiveTransform(pts1,pts2)

# def what_do(refpoint1,refpoint2,point):         #refpointy to stałe punkty, point ma być ściśle zmienny
#     a = ( refpoint2[1] - refpoint1[1] ) / ( refpoint2[0] - refpoint1[0] )
#     b = refpoint2[1] - ( a * refpoint2[0] )
#     isRaising = a > 0 ? true : false
#     y = ( a * point[0] ) + b
#     if point[1] > y:
#         return true                             #czyli krecimy zgodnie z ruchem wskazówek zegara!
#     else
#         return false                            #czyli że nie

print(findAlfaOnThreePoints((300,300),(300,0),(1500,50)))
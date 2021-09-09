import numpy as np
import sys

def checkingPoint(point, points_quad, f):
    if np.allclose(point, points_quad[0,:]) or np.allclose(point, points_quad[1,:]) or np.allclose(point, points_quad[2,:]) or np.allclose(point, points_quad[3,:]):
        f = 1
        return f
    lpFirst = locationPoint(points_quad[0,:], points_quad[1,:], points_quad[2,:], point)
    lpSecond = locationPoint(points_quad[1,:], points_quad[2,:], points_quad[3,:], point)
    lpThird = locationPoint(points_quad[2,:], points_quad[3,:], points_quad[0,:], point)
    lpFouth = locationPoint(points_quad[3,:], points_quad[0,:], points_quad[1,:], point)
    if lpFirst >= 0 and lpSecond >= 0 and lpThird >= 0 and lpFouth >= 0:
        if lpFirst == 0 or lpSecond == 0 or lpThird == 0 or lpFouth == 0:
            f = 2
            return f
        else: f = 3          
    return f

def locationPoint(pointSiseFirst,pointSideSecond,pointTop,point):
    dx = (pointSideSecond[0]-pointSiseFirst[0])
    dy = (pointSideSecond[1]-pointSiseFirst[1])
    return (dx*(point[1]-pointSiseFirst[1])-dy*(point[0]-pointSiseFirst[0]))*(dx*(pointTop[1]-pointSiseFirst[1])-dy*(pointTop[0]-pointSiseFirst[0]))

def printResult(f):
    if f == 1:
        print('точка на одной из вершин')
    elif f == 2:
        print('точка на одной из сторон')
    elif f == 3:
        print('точка внутри')
    elif f == 4:
        print('точка снаружи')

def readAndOperate(file_coord_quad, file_coord_points):
    array_coord_quad = np.loadtxt(file_coord_quad)
    array_coord_points = np.loadtxt(file_coord_points)
    for i in range(len(array_coord_points[:])):
        f = 4
        f = checkingPoint(array_coord_points[i,:], array_coord_quad, f)
        printResult(f)

if __name__ == '__main__':
    try:
        readAndOperate(sys.argv[1],sys.argv[2])
    except FileNotFoundError:
        print(f"File open failed")

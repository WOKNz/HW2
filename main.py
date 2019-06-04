from Module import Point
from Module import LineSegment
import random

if __name__ == '__main__':
    p1 = Point(1, 1)
    p2 = Point(5, 5)
    ls1 = LineSegment(p1, p2)
    p1.ownSgmnt = ls1
    p2.ownSgmnt = ls1
    p3 = Point(2,3)
    p4 = Point(3,2)
    ls2 = LineSegment(p3, p4)
    p3.ownSgmnt = ls2
    p4.ownSgmnt = ls2

    PointsList = []
    for i in range(1, 200):
        p1 = Point(random.random()*100, random.random()*100, id_=i)
        i = i + 1
        p2 = Point(random.random()*100, random.random()*100, id_=i)
        ls1 = LineSegment(p1, p2)
        p1.ownSgmnt = ls1
        p2.ownSgmnt = ls1
        PointsList.append(p1)
        PointsList.append(p2)

    Sweep = [PointsList[0]]
    Queue = []
    for Point in PointsList:
        Queue.append(Point)
    Queue.sort(key=lambda pnt: pnt.x)
    while not bool(Sweep):
        temp = Queue[0]
        Sweep.append(Queue.pop(0))
        Sweep.sort(key=lambda pnt: pnt.y)



    print('end')

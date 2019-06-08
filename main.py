from Module import Point
from Module import LineSegment
import random
import numpy as np
import pylab as pl
from matplotlib import collections  as mc

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
    for i in range(1, 40):
        p1 = Point(random.random()*100, random.random()*100, id_=i)
        i = i + 1
        p2 = Point(random.random()*100, random.random()*100, id_=i)
        if p1.x < p2.x:
            ls1 = LineSegment(p1, p2)
        else:
            ls1 = LineSegment(p2, p1)
        p1.ownSgmnt = ls1
        p2.ownSgmnt = ls1
        PointsList.append(p1)
        PointsList.append(p2)
    lines = []
    temparray = []

    i = 0
    for i in range(0, len(PointsList), 2):
        lines.append([(PointsList[i].x, PointsList[i].y), (PointsList[i+1].x, PointsList[i+1].y)])
        temparray.append([random.random(), random.random(), random.random(), random.random()])

    c = np.array(temparray)
    lc = mc.LineCollection(lines, colors=c, linewidths=1)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    fig.show()
    fig.savefig('test.pdf', format='pdf')

    Sweep = [PointsList[0].ownSgmnt]
    Queue = []
    for Point in PointsList:
        Queue.append(Point)
    Queue.sort(key=lambda pnt: pnt.x)
    while not bool(Sweep):

        if Queue[0].x == Queue[0].ownSgmnt.p1.x:
            temp = Queue[0]
            Sweep.append(Queue.pop(0).ownSgmnt)
            Sweep.sort(key=lambda pnt: pnt.y)
            Sweep.index(temp)

        elif Queue[0].x == Queue[0].ownSgmnt.p2.x:
            Sweep.append(Queue.pop(0))
            Sweep.sort(key=lambda pnt: pnt.y)
        else:
            temp = Queue[0]
            del Queue[0]
            idx = Sweep.index(temp)






    print('end')

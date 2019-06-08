import random
import numpy as np
import pylab as pl
from matplotlib import collections as mc

from Module import LineSegment
from Module import Point
from intrsect import intersect

if __name__ == '__main__':

    def search_d(inter_pnt, list_points):
        for k in list_points:
            if inter_pnt.x == k.x and inter_pnt.y == k.y:
                return True


    # Generate random Points and  Segments
    PointsList = []
    for i in range(1, 50):
        p1 = Point(random.random() * 1000, random.random() * 1000, _id=i)
        i += 1
        p2 = Point(random.random() * 1000, random.random() * 1000, _id=i)
        ls1 = LineSegment(p1, p2, i)
        p1.segment = ls1
        p2.segment = ls1
        if p1.x < p2.x:
            PointsList.append([p1, 0])
            PointsList.append([p2, 1])
        else:
            PointsList.append([p1, 1])
            PointsList.append([p2, 0])
    lines = []  # Used for initial Plot
    temparray = []  # Used for initial Plot

    # #  Manual points  Creation for special testing testing
    # p1 = Point(150, 350, _id=1)
    # p2 = Point(450, 580, _id=2)
    # ls1 = LineSegment(p1, p2, 1)
    # p1.segment = ls1
    # p2.segment = ls1
    # PointsList.append([p1, 0])
    # PointsList.append([p2, 1])
    # p1 = Point(155, 355, _id=4)
    # p2 = Point(800, 150, _id=5)
    # ls1 = LineSegment(p1, p2, 2)
    # p1.segment = ls1
    # p2.segment = ls1
    # PointsList.append([p1, 0])
    # PointsList.append([p2, 1])
    # p1 = Point(160, 600, _id=4)
    # p2 = Point(610, 20, _id=5)
    # ls1 = LineSegment(p1, p2, 2)
    # p1.segment = ls1
    # p2.segment = ls1
    # PointsList.append([p1, 0])
    # PointsList.append([p2, 1])
    # p1 = Point(750, 850, _id=4)
    # p2 = Point(870, 240, _id=5)
    # ls1 = LineSegment(p1, p2, 2)
    # p1.segment = ls1
    # p2.segment = ls1
    # PointsList.append([p1, 0])
    # PointsList.append([p2, 1])

    # Segments plot preview
    i = 0
    for i in range(0, len(PointsList), 2):
        lines.append([(PointsList[i][0].x, PointsList[i][0].y), (PointsList[i + 1][0].x, PointsList[i + 1][0].y)])
        temparray.append(
            [random.uniform(0.3, 1), random.uniform(0.3, 1), random.uniform(0.3, 1), random.uniform(0.3, 1)])

    c = np.array(temparray)
    lc = mc.LineCollection(lines, colors=c, linewidths=3)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    # fig.show()
    fig.savefig('before.pdf', format='pdf')

    # Sweep line algorithm
    T = []
    Q = PointsList
    Q.sort(key=lambda vec: vec[0].x)  # Sorting Q by x value
    T.append(Q[0][0].segment)  # Inserting initial point to T
    del Q[0]  # removing initial point from Q
    Result = []  # List of final output
    while not len(Q) == 0:  # Keep until Q empty
        if Q[0][1] == 0:  # Case for Start segment
            temp = Q[0][0]
            T.append(Q[0][0].segment)
            del Q[0]
            T.sort(key=lambda segment: segment.y_val(temp.x + 0.0001))  # Sort T by y
            index = T.index(temp.segment)
            if index + 1 < len(T):  # Checking possible neighborhood
                if intersect(T[index + 1], T[index]) is not None:  # Case for no interception
                    Result.append(intersect(T[index + 1], T[index]))  # Adding intersection to results
                    Q.append([Result[-1], 2])  # Adding intersection to Q
            if index - 1 >= 0:
                if intersect(T[index - 1], T[index]) is not None:
                    Result.append(intersect(T[index - 1], T[index]))
                    Q.append([Result[-1], 2])
            if len(Q) > 1:
                Q.sort(key=lambda vec: vec[0].x)

        elif Q[0][1] == 1:  # Case for End segment
            temp = Q[0][0]
            del Q[0]
            index = T.index(temp.segment)
            if index + 1 < len(T) and index - 1 > 0:
                if intersect(T[index + 1], T[index - 1]) is not None:
                    Result.append(intersect(T[index + 1], T[index - 1]))
                    Q.append([Result[-1], 2])
            Q.sort(key=lambda vec: vec[0].x)
            del T[index]

        else:  # Case for Intersection Point
            temp = Q[0][0]
            del Q[0]
            T.sort(key=lambda segment: segment.y_val(temp.x + 0.0001))  # Sort T by y
            id_ln1 = T.index(temp.ln1)
            id_ln2 = T.index(temp.ln2)
            if id_ln1 + 1 < len(T):
                intersect_temp = intersect(T[id_ln1 + 1], T[id_ln1])
                if intersect_temp is not None:  # Case for no interception
                    if not search_d(intersect_temp, Result):
                        Result.append(intersect_temp)
                        Q.append([Result[-1], 2])
            if id_ln1 - 1 >= 0:  # Checking possible neighborhood
                intersect_temp = intersect(T[id_ln1 - 1], T[id_ln1])
                if intersect_temp is not None:
                    if not search_d(intersect_temp, Result):
                        Result.append(intersect_temp)
                        Q.append([Result[-1], 2])
            if id_ln2 + 1 < len(T):  # Checking possible neighborhood
                intersect_temp = intersect(T[id_ln2 + 1], T[id_ln2])
                if intersect_temp is not None:
                    if not search_d(intersect_temp, Result):
                        Result.append(intersect_temp)
                        Q.append([Result[-1], 2])
            if id_ln2 - 1 >= 0:  # Checking possible neighborhood
                intersect_temp = intersect(T[id_ln2 - 1], T[id_ln2])
                if intersect_temp is not None:
                    if not search_d(intersect_temp, Result):
                        Result.append(intersect_temp)
                        Q.append([Result[-1], 2])
            Q.sort(key=lambda vec: vec[0].x)

    #  Results plot
    i = 0
    result_x = []
    result_y = []
    for pnt in Result:
        result_x.append(pnt.x)
        result_y.append(pnt.y)
    pl.scatter(result_x, result_y)
    fig.show()  # plot
    fig.savefig('after.pdf', format='pdf')

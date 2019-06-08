class LineSegment:
    def __init__(self, pnt1, pnt2, id_=None):
        """ Create a new point at the origin """
        self.id = id_
        self.p1 = pnt1
        self.p2 = pnt2


class Point:
    def __init__(self, x, y, sgmnt1: LineSegment = None, sgmnt2: LineSegment = None, id_=None):
        """ Create a new point at the origin """
        self.id = id_
        self.x = x
        self.y = y
        self.ownSgmnt = sgmnt1
        self.otherSgmnt = sgmnt2

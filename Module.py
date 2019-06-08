class Point:  # Point Class
    def __init__(self, x, y, _id=None, segment=None):
        """ Create a new point at the origin """
        self.id = _id
        self.x = x
        self.y = y
        self.segment = segment  # Attached line segment if has


class LineSegment:  # Line segment class
    def __init__(self, pnt1: Point, pnt2: Point, _id=None):
        """ Create a new point at the origin """
        self.id = _id
        if pnt1.x < pnt2.x:  # First point is always the one with lower x
            self.p1 = pnt1
            self.p2 = pnt2
        else:
            self.p2 = pnt1
            self.p1 = pnt2

    def y_val(self, x):  # Calculating y value of line from x position
        m = (self.p2.y - self.p1.y)/(self.p2.x - self.p1.x)
        test = m*(x - self.p1.x) + self.p1.y
        return test


class IntersectPoint(Point):  # Intersection point class that inheritance from Point
    def __init__(self, x, y, ln1: LineSegment, ln2: LineSegment, _id=None):
        super().__init__(x, y, _id)  # Passing to Point
        self.ln1 = ln1
        self.ln2 = ln2

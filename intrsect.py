from Module import Point


def intersect(p1, p2, q1, q2):
    line1 = [[p1.x, p1.y], [p2.x, p2.y]]
    line2 = [[q1.x, q1.y], [q2.x, q2.y]]
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return Point(x, y)

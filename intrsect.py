from Module import IntersectPoint


def intersect(line_a, line_b):  # Intersection from Determinants

    line1 = [[line_a.p1.x, line_a.p1.y], [line_a.p2.x, line_a.p2.y]]
    line2 = [[line_b.p1.x, line_b.p1.y], [line_b.p2.x, line_b.p2.y]]
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    
    if x < line1[1][0] and x < line2[1][0]:  # Make sure the intersection is in boundaries
        if x > line1[0][0] and x > line2[0][0]:
            return IntersectPoint(x, y, line_a, line_b)  # Returning IntersectionPoint

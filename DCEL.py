import math


def iscw(list_of_points):
    sum_of_x = 0
    sum_of_y = 0
    for point in list_of_points:
        sum_of_x += point[0]
        sum_of_y += point[1]
    x = sum_of_x / len(list_of_points)
    y = sum_of_y / len(list_of_points)
    return (math.atan2(list_of_points[1][1] - y, list_of_points[1][0] - x) - math.atan2(list_of_points[0][1] - y,
                                                                                        list_of_points[0][0] - x)) < 0


class Edge:
    def __init__(self, p1, p2, name=None):
        self.name = name
        self.p1 = p1
        self.p2 = p2


class Vertex:
    def __init__(self, name, p1, incidentedge: Edge):
        self.name = name
        self.p1 = p1
        self.incidentedge = incidentedge


class Face:
    def __init__(self, name, inner_component, outer_component):
        self.inn = inner_component
        self.out = outer_component


class HalfEdge:
    def __init__(self, half_edge: Edge, origin: Vertex, twin: Edge, incident_face: Face, next_edge=None,
                 prev_edge=None):
        self.half_edge = half_edge
        self.origin = origin
        self.twin = twin
        self.incident_face = incident_face
        self.next_edge = next_edge
        self.prev_edge = prev_edge

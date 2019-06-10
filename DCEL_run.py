import matplotlib.pyplot as plt

from DCEL import Edge
from DCEL import Face
from DCEL import HalfEdge
from DCEL import Vertex
from DCEL import iscw


def nametest(compare_point, listofvertex,
             what_to_return=None):  # Method that checks if point is already in vertexes and returns it if needed
    if what_to_return == 1:
        for vertex2 in listofvertex:
            if compare_point == vertex2.p1:
                return True
    else:
        for vertex2 in listofvertex:
            if compare_point == vertex2.p1:
                return vertex2.name


if __name__ == '__main__':

    # Cases for line input
    countENT = False
    countLW = False
    countPAR = False
    countX = False
    countY = False
    temp_x = None
    temp_y = None
    list_of_points = []
    temp_i = None

    with open('HW2.dxf', "r", encoding="utf8") as lines:
        list_of_poly = []
        for i, line in enumerate(lines):
            if line == "ENTITIES\n":  # Start block
                countENT = True
                continue
            if line == "LWPOLYLINE\n" and countENT:  # Start block
                countLW = True
            if line == "PARCELS\n" and countLW:  # Start block
                countPAR = True
            if line == " 10\n" and countLW and countPAR:  # Start block X
                temp_i = 'x'
                continue
            if temp_i == 'x':
                temp_x = float(line.replace('\n', ''))
                temp_i = None
                countX = True
            if line == " 20\n" and countLW and countPAR:  # Start block Y
                temp_i = 'y'
                continue
            if temp_i == 'y':
                temp_y = float(line.replace('\n', ''))
                temp_i = None
                countY = True
            if countX and countY:  # Reset
                list_of_points.append([temp_x, temp_y])
                temp_x = None
                temp_y = None
                countX = False
                countY = False
            if line == "1001\n" and countPAR:  # Close Block
                countLW = False
                countPAR = False
                list_of_poly.append(list_of_points.copy())  # Add point to PARCEL
                list_of_points.clear()

    for polygon in list_of_poly:  # Fix Direction of points in polygon
        if iscw(polygon):
            polygon.reverse()

    vertex_list = []
    counter = 0
    face_id = []

    for poly in list_of_poly:  # Close loop with adding first point to the end
        poly.append(poly[-1])

    for k, poly in enumerate(list_of_poly):  # 4 Cases of points
        for i in range(0, len(poly) - 1):
            if nametest(poly[i], vertex_list, 1) and nametest(poly[i + 1], vertex_list, 1):  # Both Vertexes exist
                temp_name1 = nametest(poly[i], vertex_list)
                temp_name2 = nametest(poly[i + 1], vertex_list)
                vertex_list.append(Vertex(temp_name1, poly[i],
                                          Edge(poly[i], poly[i + 1], 'e' + temp_name1 + '-' + temp_name2)))
                face_id.append(k)
            if nametest(poly[i], vertex_list, 1) and not nametest(poly[i + 1], vertex_list, 1):  # One Vertexes exist
                temp_name1 = nametest(poly[i], vertex_list)
                counter += 1
                temp_name2 = 'v' + str(counter)
                vertex_list.append(Vertex(temp_name1, poly[i],
                                          Edge(poly[i], poly[i + 1], 'e' + temp_name1 + '-' + temp_name2)))
                face_id.append(k)
            if not nametest(poly[i], vertex_list, 1) and nametest(poly[i + 1], vertex_list, 1):  # One Vertexes exist
                counter += 1
                temp_name1 = 'v' + str(counter)
                temp_name2 = nametest(poly[i + 1], vertex_list)
                vertex_list.append(Vertex(temp_name1, poly[i],
                                          Edge(poly[i], poly[i + 1], 'e' + temp_name1 + '-' + temp_name2)))
                face_id.append(k)
            if not nametest(poly[i], vertex_list, 1) and not nametest(poly[i + 1], vertex_list,
                                                                      1):  # None Vertexes exist
                counter += 1
                temp_name1 = 'v' + str(counter)
                temp_name2 = 'v' + str(counter + 1)
                vertex_list.append(Vertex(temp_name1, poly[i],
                                          Edge(poly[i], poly[i + 1], 'e' + temp_name1 + '-' + temp_name2)))
                face_id.append(k)

            # Resseting temps
            temp_name1 = None
            temp_name2 = None

    edge_list = []

    for k, vertex in enumerate(vertex_list):  # Creating list of edges and faces inside
        edge_list.append(HalfEdge(vertex.incidentedge, vertex, Edge(vertex.incidentedge.p2, vertex.incidentedge.p1),
                                  Face('f' + str(face_id[k]), vertex.incidentedge, None)))

    clean_list_vertex = vertex_list
    temp_range = len(clean_list_vertex) - 1

    for k in range(0, temp_range):  # Reducing Duplicate vertexes
        for j in range(k+1, temp_range-1):
            if clean_list_vertex[k].name == clean_list_vertex[j].name:
                del clean_list_vertex[j]
                temp_range -= 1

    # Plot Vertexes
    for i in range(0, len(clean_list_vertex) - 2):
        plt.plot(clean_list_vertex[i].p1[0], clean_list_vertex[i].p1[1], 'go--')
    plt.show()

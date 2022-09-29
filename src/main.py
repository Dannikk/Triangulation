import argparse
import numpy as np
from geometry import is_it_convex, is_it_ear
from doubly_connected_vertex_list import DCVL, Vertex, Direction
import matplotlib.pyplot as plt
from random import randrange


def read_vertices(file_name: str):
    file = open(file_name, 'r')
    point = np.array(list(map(lambda x: float(x), file.readline().split())))
    dcel = DCVL()

    v = Vertex(point)
    right_vertex = v
    dcel.add_vertex(v)
    vert_counter = 1
    for string in file:
        point = np.array(list(map(lambda x: float(x), string.split())))
        u = Vertex(point)
        right_vertex = u if u.get_x() > right_vertex.get_x() else right_vertex
        dcel.add_vertex(u)
        vert_counter += 1
    file.close()
    if vert_counter <= 3:
        return None, 'The number of vertices is less than or equal to 3'

    if right_vertex.prev.get_y() < right_vertex.next_vertex.get_y():
        dcel.set_direction(Direction.COUNTERCLOCKWISE)
    else:
        dcel.set_direction(Direction.CLOCKWISE)
    return dcel, 'Polygon vertices read'


def triangulation(dcvl: DCVL):

    vertex = dcvl.current
    while dcvl.count > 3:
        if is_it_convex(vertex, dcvl) and is_it_ear(vertex, dcvl):
            yield vertex.prev.point, vertex.point, vertex.next_vertex.point
            vertex = dcvl.delete_vertex()
            if is_it_ear(vertex, dcvl) and is_it_ear(vertex, dcvl):
                continue
            elif is_it_ear(vertex.next_vertex, dcvl) and is_it_ear(vertex.next_vertex, dcvl):
                vertex = dcvl.get_next()
                continue

        vertex = dcvl.get_next()
    vertex = dcvl.current
    yield vertex.prev.point, vertex.point, vertex.next_vertex.point


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Triangulation")
    parser.add_argument('input', type=str, help='direction to input file')
    parser.add_argument('-show', action="store_true", help='choose to draw polygon triangulation')
    parser.add_argument('-out', type=str, help='direction to output file', default='output.txt')
    args = parser.parse_args()
    input_file = args.input
    show = args.show
    output_file = args.out
    print(f"File to read polygon vertices:\t\t{args.input}")
    print(f"File to write triangulation vertices:\t{args.out}")
    print(f"Visualize triangulation in matplotlib:\t{args.show}")

    dcvl, msg = read_vertices(input_file)
    print(msg)

    if show:
        fig = plt.figure(figsize=(9, 12))
        ax = fig.add_subplot(111)
    file = open(output_file, 'w')
    for m, n, k in triangulation(dcvl):
        file.write(f'{m[0]} {m[1]} {n[0]} {n[1]} {k[0]} {k[1]}\n')
        if show:
            trian = np.column_stack((m, n, k))
            color = [randrange(0, 255, 2)/255 for _ in range(3)]
            ax.fill(trian[0], trian[1], color=color)
    file.close()
    if show:
        plt.grid()
        plt.show()

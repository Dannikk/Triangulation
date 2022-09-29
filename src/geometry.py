import numpy as np
from doubly_connected_vertex_list import Vertex, DCVL


def parallelogram_square(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> float:
    """
    If a, b, c points form a left turn in a triangle
    then the return value is positive, and negative otherwise
    """
    ones = np.ones(3)
    matrix = np.column_stack((np.row_stack((a, b, c)), ones))
    return np.linalg.det(matrix)


def is_point_in_triangle(p: np.ndarray, a: np.ndarray, b: np.ndarray, c: np.ndarray, dir_coef: int = 1) -> bool:
    if parallelogram_square(p, a, b)*dir_coef > 0 and parallelogram_square(p, b, c)*dir_coef > 0 and \
            parallelogram_square(p, c, a)*dir_coef > 0:
        return True
    else:
        return False


def is_it_convex(v: Vertex, dcvl: DCVL):
    a = v.prev.point
    b = v.point
    c = v.next_vertex.point
    if parallelogram_square(a, b, c) * dcvl.direction.value > 0:
        return True
    else:
        return False


def is_it_ear(v: Vertex, dcvl: DCVL):
    other_v = v.next_vertex
    prev_v = v.prev
    next_v = v.next_vertex
    curr_v = v
    for _ in range(dcvl.count-3):
        other_v = other_v.next_vertex
        if not is_point_in_triangle(other_v.point, prev_v.point, curr_v.point, next_v.point, dcvl.direction.value):
            continue
        else:
            return False
    return True

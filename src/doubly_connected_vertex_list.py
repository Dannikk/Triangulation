from enum import Enum


class Direction(Enum):
    CLOCKWISE = -1
    COUNTERCLOCKWISE = 1


class DCVL:

    def __init__(self):
        self.count: int = 0
        self.head: Vertex = None
        self.tail: Vertex = None
        self.current: Vertex = None
        self.direction: Direction = None

    def add_vertex(self, vertex):
        if self.count == 0:
            self.head = vertex
            self.tail = vertex
            self.current = vertex
            self.count += 1
        else:
            next_v = self.current.next_vertex
            vertex.next_vertex = next_v if next_v != self.tail else self.tail
            vertex.prev = self.current
            self.current.next_vertex = vertex
            self.current = vertex
            self.count += 1

    def get_next(self):
        self.current = self.current.next_vertex
        return self.current

    def delete_vertex(self):
        self.count -= 1
        prev = self.current.prev
        next_vertex = self.current.next_vertex
        prev.next_vertex = next_vertex
        next_vertex.prev = prev
        self.current = prev

        return prev

    def set_direction(self, direction: Direction):
        self.direction = direction

    def print_list(self):
        v = self.current
        for _ in range(self.count):
            print(v.point, end='')
            v = v.next_vertex
        print()


class Vertex:

    def __init__(self, point):
        self.point = point
        self.prev = self
        self.next_vertex = self

    def get_x(self):
        return self.point[0]

    def get_y(self):
        return self.point[1]

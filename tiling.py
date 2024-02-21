# Inspired by https://github.com/fogleman/Tiling

from math import pi, tan
from vec import Vec
from system import Particle, Link

##############################################################################################


class Shape(object):
    def __init__(self, side_count, pos=Vec(0, 0), rotation=0):
        self.side_count = side_count
        self.pos = pos
        self.rotation = rotation

    def copy(self, pos):
        return Shape(self.side_count, pos=pos, rotation=self.rotation)

    def points(self):
        points = []
        step_angle = 2*pi / self.side_count
        for i in range(self.side_count):
            angle = self.rotation + i*step_angle
            pos = self.pos + Vec.new_polar(1, angle)
            points.append(pos)
        return points

    def adjacent(self, side_count, edge):
        points = self.points()
        point_1, point_2 = points[edge], points[(edge + 1) % self.side_count]
        edge_midpoint = (point_1 + point_2) / 2
        edge_vector = point_2 - point_1
        edge_angle = edge_vector.angle()
        edge_length = edge_vector.mag()
        dist_to_center = edge_length / (2*tan(pi / side_count))
        new_pos = edge_midpoint + \
            Vec.new_polar(dist_to_center, edge_angle + pi / 2)
        new_angle = edge_angle + pi / side_count
        return Shape(side_count, new_pos, new_angle)

    def __eq__(self, other):
        return (self.side_count == other.side_count and
                self.pos == other.pos and
                self.rotation == other.rotation)

    def __hash__(self):
        return hash((self.side_count, self.pos, self.rotation))

##############################################################################################


class Tiling(object):
    def __init__(self, width=10, height=10, scale=10):
        self.width = width
        self.height = height
        self.scale = scale
        self.shapes = set()

    def add(self, shape):
        self.shapes.add(shape)
        return shape

    def add_adjacent(self, to_shape, side_count, edge):
        new_shape = to_shape.adjacent(side_count, edge)
        self.add(new_shape)
        return new_shape

    def duplicate(self, offset):
        duplicates = []
        for shape in self.shapes:
            dublicate = shape.copy(shape.pos + offset)
            self.add(duplicate)
            duplicates.append(duplicate)
        return duplicates

    def _repeat(self, indexes, x, y, depth, memo):
        if depth < 0:
            return
        key = normalize(x, y)
        previous_depth = memo.get(key, -1)
        if previous_depth >= depth:
            return
        memo[key] = depth
        if previous_depth == -1:
            self.add_repeats(x, y)
        for index in indexes:
            shape = self.shapes[index]
            self._repeat(
                indexes, x + shape.x, y + shape.y, depth - 1, memo)

    def repeat(self, indexes):
        memo = {}
        depth = 0
        while True:
            self._repeat(indexes, 0, 0, depth, memo)
            w = self.width / 2.0 / self.scale
            h = self.height / 2.0 / self.scale
            tl = any(x < -w and y < -h for x, y in memo)
            tr = any(x > w and y < -h for x, y in memo)
            bl = any(x < -w and y > h for x, y in memo)
            br = any(x > w and y > h for x, y in memo)
            if tl and tr and bl and br:
                break
            depth += 1

    def particles(self):
        pass

    def links(self):
        pass

##############################################################################################

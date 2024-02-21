# Inspired by https://github.com/fogleman/Tiling

from math import pi, tan, sin
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
            pos = self.pos + \
                Vec.new_polar(1 / (2*sin(pi/self.side_count)), angle)
            points.append(pos)
        return points

    def adjacent(self, edge, side_count):
        points = self.points()
        point_1, point_2 = points[edge], points[(edge + 1) % self.side_count]
        edge_midpoint = (point_1 + point_2) / 2
        edge_vector = point_2 - point_1
        edge_angle = edge_vector.angle()
        dist_to_center = 1 / (2*tan(pi / side_count))
        new_pos = edge_midpoint + \
            Vec.new_polar(dist_to_center, edge_angle - pi / 2)
        # point perpendicular to edge, then if it's even sided adjust by an amount of the internal angle
        new_angle = edge_angle - pi/2 - ((side_count - 1) % 2)*pi/side_count
        return Shape(side_count, pos=new_pos, rotation=new_angle)

    def __eq__(self, other):
        return (self.side_count == other.side_count and
                self.pos == other.pos and
                self.rotation == other.rotation)

    def __hash__(self):
        return hash((self.side_count, self.pos, self.rotation))

##############################################################################################


class Tiling(object):
    def __init__(self):
        self.shapes = set()

    def add(self, shape):
        self.shapes.add(shape)
        return shape

    def add_adjacent(self, to_shape, edge, side_count):
        new_shape = to_shape.adjacent(edge, side_count)
        self.add(new_shape)
        return new_shape

    def duplicate(self, offset):
        duplicates = []
        for shape in self.shapes:
            duplicates.append(shape.copy(shape.pos + offset))
        for shape in duplicates:
            self.add(shape)
        return duplicates

    def to_system(self):
        particles = set()
        links = set()
        for shape in self.shapes:
            points = shape.points()
            for i, point in enumerate(points):
                start = Particle(pos=point)
                end = Particle(pos=points[(i+1) % shape.side_count])
                particles.update((start, end))
                links.add(Link(start, end))
            links.add(Link(Particle(pos=points[0]), Particle(pos=points[-1])))
        return (particles, links)
##############################################################################################

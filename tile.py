# Adapted from https://github.com/fogleman/Tiling

from math import sin, cos, tan, pi, atan2
from vec import Vec
from particle import Particle
from interaction import Link

from math import sin, cos, tan, pi, atan2

# Model() defaults
WIDTH = 10
HEIGHT = 10
SCALE = 10

def normalize(x, y):
    return (round(x, 6), round(y, 6))

def inset_corner(p1, p2, p3, margin):
    (x1, y1), (x2, y2), (x3, y3) = (p1, p2, p3)
    a1 = atan2(y2 - y1, x2 - x1) - pi / 2
    a2 = atan2(y3 - y2, x3 - x2) - pi / 2
    ax1, ay1 = x1 + cos(a1) * margin, y1 + sin(a1) * margin
    ax2, ay2 = x2 + cos(a1) * margin, y2 + sin(a1) * margin
    bx1, by1 = x2 + cos(a2) * margin, y2 + sin(a2) * margin
    bx2, by2 = x3 + cos(a2) * margin, y3 + sin(a2) * margin
    ady, adx = ay2 - ay1, ax1 - ax2
    bdy, bdx = by2 - by1, bx1 - bx2
    c1 = ady * ax1 + adx * ay1
    c2 = bdy * bx1 + bdx * by1
    d = ady * bdx - bdy * adx
    x = (bdx * c1 - adx * c2) / d
    y = (ady * c2 - bdy * c1) / d
    return (x, y)

def inset_polygon(points, margin):
    result = []
    points = list(points)
    points.insert(0, points[-2])
    for p1, p2, p3 in zip(points, points[1:], points[2:]):
        point = inset_corner(p1, p2, p3, margin)
        result.append(point)
    result.append(result[0])
    return result

class Shape(object):
    def __init__(self, sides, x=0, y=0, rotation=0, **kwargs):
        self.sides = sides
        self.x = x
        self.y = y
        self.rotation = rotation
        for key, value in kwargs.items():
            setattr(self, key, value)
    def copy(self, x, y):
        return Shape(
            self.sides, x, y, self.rotation,
        )
    def points(self, margin=0):
        angle = 2 * pi / self.sides
        rotation = self.rotation - pi / 2
        if self.sides % 2 == 0:
            rotation += angle / 2
        angles = [angle * i + rotation for i in range(self.sides)]
        angles.append(angles[0])
        d = 0.5 / sin(angle / 2) - margin / cos(angle / 2)
        return [(self.x + cos(a) * d, self.y + sin(a) * d) for a in angles]
    def adjacent(self, sides, edge, **kwargs):
        (x1, y1), (x2, y2) = self.points()[edge:edge + 2]
        angle = 2 * pi / sides
        a = atan2(y2 - y1, x2 - x1)
        b = a - pi / 2
        d = 0.5 / tan(angle / 2)
        x = x1 + (x2 - x1) / 2.0 + cos(b) * d
        y = y1 + (y2 - y1) / 2.0 + sin(b) * d
        a += angle * ((sides - 1) // 2)
        return Shape(sides, x, y, a, **kwargs)

class Model(object):
    def __init__(self, width=WIDTH, height=HEIGHT, scale=SCALE):
        self.width = width
        self.height = height
        self.scale = scale
        self.shapes = []
        self.lookup = {}
    def append(self, shape):
        self.shapes.append(shape)
        key = normalize(shape.x, shape.y)
        self.lookup[key] = shape
        return len(self.shapes) - 1
    def _add(self, index, edge, sides, **kwargs):
        parent = self.shapes[index]
        shape = parent.adjacent(sides, edge, **kwargs)
        self.append(shape)
    def add(self, indexes, edges, sides, **kwargs):
        if isinstance(indexes, int):
            indexes = [indexes]
        if isinstance(edges, int):
            edges = [edges]
        start = len(self.shapes)
        for index in indexes:
            for edge in edges:
                self._add(index, edge, sides, **kwargs)
        end = len(self.shapes)
        return range(start, end)
    def add_repeats(self, x, y):
        for shape in self.shapes:
            key = normalize(x + shape.x, y + shape.y)
            if key in self.lookup:
                continue
            self.lookup[key] = shape.copy(x + shape.x, y + shape.y)
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
        vertices = set()
        for shape in self.lookup.values():
            for point in shape.points():
                vertices.add(normalize(*point))

        particles = []
        for vertex in vertices:
            particles.append(Particle(pos=Vec(vertex[0], vertex[1], 0)))

        return particles
    def edges(self):
        edges = set()
        for shape in self.lookup.values():
            points = shape.points()
            for i in range(len(points) - 1):
                start_point = normalize(*points[i])
                end_point = normalize(*points[i + 1])
                edge = (start_point, end_point)
                edges.add(edge)
        return list(edges)

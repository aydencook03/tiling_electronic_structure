from math import pi, tan, sin
from vec import Vec
from system import Particle, Link

##############################################################################################


class Shape(object):
    """
    Abstractly represents a shape (regular polygon) with a position, rotation, side count, and side length.
    """

    def __init__(self, side_count, side_length=1, pos=Vec(0, 0), rotation=0):
        self.side_count = side_count
        self.side_length = side_length
        self.pos = pos
        self.rotation = rotation

    def copy(self, pos):
        """
        Returns a copy of the shape at a new position.
        """
        return Shape(self.side_count, side_length=self.side_length, pos=pos, rotation=self.rotation)

    def points(self):
        """
        Calculates and returns a list of points associated with the vertices of the shape.
        """
        points = []
        step_angle = 2*pi / self.side_count
        for i in range(self.side_count):
            angle = self.rotation + i*step_angle
            pos = self.pos + \
                Vec.new_polar(self.side_length /
                              (2*sin(pi/self.side_count)), angle)
            points.append(pos)
        return points

    def adjacent(self, edge, side_count):
        """
        Calculates and returns a new shape with `side_count` sides that is adjacent to an edge of this one.
        """
        points = self.points()
        point_1, point_2 = points[edge], points[(edge + 1) % self.side_count]
        edge_midpoint = (point_1 + point_2) / 2
        edge_vector = point_2 - point_1
        edge_angle = edge_vector.angle()
        dist_to_center = self.side_length / (2*tan(pi / side_count))
        new_pos = edge_midpoint + \
            Vec.new_polar(dist_to_center, edge_angle - pi / 2)
        # point perpendicular to edge, then if it's even sided adjust by an amount of the internal angle
        new_angle = edge_angle - pi/2 - ((side_count - 1) % 2)*pi/side_count
        return Shape(side_count, side_length=self.side_length, pos=new_pos, rotation=new_angle)

    def __eq__(self, other):
        return (self.side_count == other.side_count and
                self.pos == other.pos and
                self.rotation == other.rotation)

    def __hash__(self):
        return hash((self.side_count, self.pos, self.rotation))

##############################################################################################


class Tiling(object):
    """
    Represents a collection of shapes.
    """

    def __init__(self):
        self.shapes = set()

    def add(self, shape):
        """
        Adds a new shape to the tiling.
        """
        self.shapes.add(shape)
        return shape

    def add_adjacent(self, to_shape, edge, side_count):
        """
        Adds a new shape with `side_count` sides that is adjacent to the edge of another shape.
        """
        new_shape = to_shape.adjacent(edge, side_count)
        self.add(new_shape)
        return new_shape

    def duplicate(self, pos):
        """
        Duplicates the current set of shapes at another position.
        """
        duplicates = []
        for shape in self.shapes:
            duplicates.append(shape.copy(pos))
        for shape in duplicates:
            self.add(shape)
        return duplicate

    def add_unit_pattern(self, unit, side_length=1, pos=Vec(0, 0), rotation=0, depth=3):
        repeats = set()
        unit(self, side_length, pos, rotation, repeats)
        if depth > 1:
            for shape in repeats:
                self.add_unit_pattern(unit, side_length=side_length,
                                 pos=shape.pos, rotation=rotation, depth=depth-1)

        return self

    def add_to_system(self, system):
        """
        Returns the sets of particles and links associated with all of the shapes' vertices and edges.
        """
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
        if system is not None:
            system.add_particles(particles)
            system.add_links(links)
        return (particles, links)

##############################################################################################

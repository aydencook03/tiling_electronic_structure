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

    def points(self):
        points = set()
        for shape in self.shapes:
            points.update(shape.points())
        return points

    def add_unit_pattern(self, unit_generator, side_length=1, pos=Vec(0, 0), rotation=0, depth=1, called=False):
        repeats = []
        unit_generator(self, side_length, pos, rotation, repeats)
        if not called:
            self.lattice_vectors = [repeats[0].pos - pos, repeats[1].pos - pos]
            self.unit_coordinates = []
            self.center = pos
            for point in self.points():
                basis_1, basis_2 = self.lattice_vectors
                x = Vec.cross(point - pos, basis_2)/Vec.cross(basis_1, basis_2)
                y = Vec.cross(point - pos, basis_1)/Vec.cross(basis_1, basis_2)
                self.unit_coordinates.append([x, y])
        if depth > 1:
            for shape in repeats:
                self.add_unit_pattern(unit_generator, side_length=side_length,
                                      pos=shape.pos, rotation=rotation, depth=depth-1, called=True)
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

        system.test = [self.center,
                       self.lattice_vectors, self.unit_coordinates]

        return (particles, links)

##############################################################################################

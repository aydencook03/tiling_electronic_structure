from math import pi, tan, sin
from vec import Vec

##############################################################################################


class Edge:
    """
    Represents a **hashable** connection between two points.
    """

    def __init__(self, point_1, point_2):
        self.points = frozenset((point_1, point_2))

    def __eq__(self, other):
        return isinstance(other, Edge) and self.points == other.points

    def __hash__(self):
        return hash(self.points)

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

    def points_edges(self):
        """
        Returns the lists of points and edges (pairs of point indices) associated with the tiling.
        """
        points = set()
        edges = set()
        for shape in self.shapes:
            shape_points = shape.points()
            for i, point in enumerate(shape_points):
                start = point
                end = shape_points[(i+1) % shape.side_count]
                points.update((start, end))
                edges.add(Edge(start, end))
            edges.add(Edge(shape_points[0], shape_points[-1]))
        return_points = list(points)
        return_edges = []
        for edge in edges:
            edge_points = list(edge.points)
            return_edges.append([return_points.index(edge_points[0]),
                                 return_points.index(edge_points[1])])
        return (return_points, return_edges)

    def add_unit_pattern(self, unit_generator, side_length=1, pos=Vec(0, 0), rotation=0, depth=1, called=False):
        """
        Uses a unit generator to generate a tiling and add it to the set of shapes.
        Depth can be changed to vary how many times the unit is duplicated and tiled across the plane.
        Automatically creates the associated lattice vectors, vertex (orbital) coordinates, and hopping pairs (edges).
        """
        repeats = []
        unit_generator(self, side_length, pos, rotation, repeats)
        if not called:
            basis_1, basis_2 = repeats[0].pos - pos, repeats[1].pos - pos
            self.lattice_vectors = [basis_1, basis_2] if Vec.cross(
                # pythtb wants a right-handed coord system
                basis_1, basis_2) > 0 else [basis_2, basis_1]
            points, self.hop_pairs = self.points_edges()
            self.unit_coordinates = [None]*len(points)
            for i, point in enumerate(points):
                basis_1, basis_2 = self.lattice_vectors
                x = Vec.cross(point - pos, basis_2)/Vec.cross(basis_1, basis_2)
                y = Vec.cross(point - pos, basis_1)/Vec.cross(basis_2, basis_1)
                self.unit_coordinates[i] = [x, y]
        if depth > 1:
            for shape in repeats:
                self.add_unit_pattern(unit_generator, side_length=side_length,
                                      pos=shape.pos, rotation=rotation, depth=depth-1, called=True)
        return self

    def render_full(self, pyplot, debug=False, title="Full Tiling", show_points=False, show_edges=True, png=False):
        """
        Render the full tiling to a matplotlib instance.
        This is helpful when creating a new unit to ensure that it properly tiles the plane.
        """
        figure = pyplot.figure(title)
        axes = figure.add_subplot()
        pyplot.title(title)
        points, edges = self.points_edges()
        if show_points:
            for point in points:
                if debug:
                    import random
                    axes.scatter(point.x - 0.2 + random.random()
                                 * 0.4, point.y - 0.2 + random.random()
                                 * 0.4, color="black")
                else:
                    axes.scatter(point.x, point.y, color="black")
        if show_edges:
            for edge in edges:
                x = [points[i].x for i in edge]
                y = [points[i].y for i in edge]
                axes.plot(x, y, color="black")
        axes.set_xlabel("x")
        axes.set_ylabel("y")
        axes.set_aspect("equal")
        if debug:
            print(title)
            print("Point List Count: {}".format(len(points)))
            print("Point Set Count: {}".format(len(set(points))))
            print("Edge List Count: {}".format(len(edges)))
            print("Edge Set Count: {}\n".format(
                len(set(map(lambda edge: Edge(*edge), edges)))))
        if png:
            pyplot.savefig("images/{}.png".format(title), dpi=400)
        else:
            pyplot.show()

    def render_unit(self, pyplot, title="Tiling Unit", png=False):
        """
        Utility function to render all of the unit cell data.
        Shows the index of each vertex, edge, and lattice vector so you can pick hopping parameters, onsite energies, etc.
        """
        basis = self.lattice_vectors
        coords = self.unit_coordinates
        pairs = self.hop_pairs
        figure = pyplot.figure(title)
        axes = figure.add_subplot()
        pyplot.title(title)
        for i, vec in enumerate(basis):
            axes.quiver([0], [0], [vec.x], [vec.y],
                        angles='xy', scale_units='xy', scale=1)
            axes.annotate(str(i), xy=(vec.x, vec.y), xytext=(vec.x + 0.2, vec.y + 0.2),
                          textcoords="offset points", fontsize=10)
        for i, pair in enumerate(pairs):
            start = Vec.from_coords(coords[pair[0]], basis)
            end = Vec.from_coords(coords[pair[1]], basis)
            mid = (start + end)/2
            axes.plot([start.x, end.x], [start.y, end.y], color="blue")
            axes.annotate(str(i), xy=(mid.x, mid.y), xytext=(mid.x + 0.2, mid.y + 0.2),
                          textcoords="offset points", fontsize=10, color="blue")
        for i, coord in enumerate(coords):
            pos = Vec.from_coords(coord, basis)
            axes.scatter([pos.x], [pos.y], color="red")
            axes.annotate(str(i), xy=(pos.x, pos.y), xytext=(pos.x + 0.2, pos.y + 0.2),
                          textcoords="offset points", fontsize=10, color="red")
        axes.set_xlabel("x")
        axes.set_ylabel("y")
        axes.set_aspect("equal")
        if png:
            pyplot.savefig("images/{}.png".format(title), dpi=400)
        else:
            pyplot.show()

##############################################################################################

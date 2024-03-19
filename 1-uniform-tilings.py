from vec import Vec
from system import System
from tiling import Shape, Tiling
import matplotlib.pyplot as plot

##############################################################################################
# The 1-Uniform Tilings


def hexagon(pos=Vec(0, 0), side_length=1, rotation=0, repeated=False):
    """
    A hexagon with a hexagon on each side.
    """
    tiling = Tiling()
    hexagon = tiling.add(
        Shape(6, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(6):
        hexagon_2 = tiling.add_adjacent(hexagon, i, 6)
    if repeated:
        pass
    return tiling


def octagon_square(pos=Vec(0, 0), side_length=1, rotation=0, repeated=False):
    """
    An octagon with 4 surrounding squares.
    """
    tiling = Tiling()
    octagon = tiling.add(
        Shape(8, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(4):
        square = tiling.add_adjacent(octagon, 2*i, 4)
        octagon_2 = tiling.add_adjacent(octagon, 2*i+1, 8)
    if repeated:
        pass
    return tiling


def dodecagon_hexagon_square(pos=Vec(0, 0), side_length=1, rotation=0, repeated=False):
    """
    A dodecagon surrounded by alternating hexagons and squares.
    """
    tiling = Tiling()
    dodecagon = tiling.add(
        Shape(12, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(6):
        square = tiling.add_adjacent(dodecagon, 2*i, 4)
        hexagon = tiling.add_adjacent(dodecagon, 2*i+1, 6)
    if repeated:
        pass
    return tiling


def dodecagon_triangle(pos=Vec(0, 0), side_length=1, rotation=0, repeated=False):
    """
    A dodecagon surrounded by triangles and dodecagons.
    """
    tiling = Tiling()
    dodecagon = tiling.add(
        Shape(12, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(6):
        triangle = tiling.add_adjacent(dodecagon, 2*i, 3)
        dodecagon_2 = tiling.add_adjacent(dodecagon, 2*i+1, 12)
    if repeated:
        pass
    return tiling


def square(pos=Vec(0, 0), side_length=1, rotation=0, repeated=False):
    """
    A square with a square on each side.
    """
    tiling = Tiling()
    square = tiling.add(
        Shape(4, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(4):
        square_2 = tiling.add_adjacent(square, i, 4)
        square_3 = tiling.add_adjacent(square_2, 1, 4)
    if repeated:
        pass
    return tiling


def hexagon_square_triangle(pos=Vec(0, 0), side_length=1, rotation=0, repeated=False):
    """
    A hexagon with squares on each side. The squares have triangles on their sides.
    """
    tiling = Tiling()
    hexagon = tiling.add(
        Shape(6, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(6):
        square = tiling.add_adjacent(hexagon, i, 4)
        triangle = tiling.add_adjacent(square, 1, 3)
    if repeated:
        pass
    return tiling


def hexagon_triangle(pos=Vec(0, 0), side_length=1, rotation=0, repeated=False):
    """
    A hexagon with a triangle on each side. Star of David.
    """
    tiling = Tiling()
    hexagon = tiling.add(
        Shape(6, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(6):
        triangle = tiling.add_adjacent(hexagon, i, 3)
        hexagon_2 = tiling.add_adjacent(triangle, 0, 6)
        triangle_2 = tiling.add_adjacent(hexagon_2, 1, 3)
    if repeated:
        pass
    return tiling


def square_triangle(pos=Vec(0, 0), side_length=1, rotation=0, repeated=False):
    """
    Alternating strips of squares and triangles.
    """
    tiling = Tiling()
    square = tiling.add(
        Shape(4, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(2):
        triangle = tiling.add_adjacent(square, 2*i, 3)
        square_2 = tiling.add_adjacent(square, 2*i+1, 4)
        triangle_2 = tiling.add_adjacent(square_2, 1, 3)
        triangle_3 = tiling.add_adjacent(square_2, 3, 3)
        triangle_4 = tiling.add_adjacent(triangle, 0, 3)
        triangle_5 = tiling.add_adjacent(triangle_2, 0, 3)
    if repeated:
        pass
    return tiling


def square_triangle_square(pos=Vec(0, 0), side_length=1, rotation=0, repeated=False):
    """
    Square surrounded by triangles that have squares on them.
    """
    tiling = Tiling()
    square = tiling.add(
        Shape(4, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(4):
        triangle = tiling.add_adjacent(square, i, 3)
        square_2 = tiling.add_adjacent(triangle, 0, 4)
        triangle_2 = tiling.add_adjacent(triangle, 2, 3)
    if repeated:
        pass
    return tiling


def hexagon_triangle_triangle(pos=Vec(0, 0), side_length=1, rotation=0, repeated=False):
    """
    Hexagon surrounded by triangles that have triangles on them.
    """
    tiling = Tiling()
    hexagon = tiling.add(
        Shape(6, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(6):
        triangle = tiling.add_adjacent(hexagon, i, 3)
        triangle_2 = tiling.add_adjacent(triangle, 0, 3)
        triangle_3 = tiling.add_adjacent(triangle, 2, 3)
    if repeated:
        pass
    return tiling


def triangle(pos=Vec(0, 0), side_length=1, rotation=0, repeated=False):
    """
    Triangle surrounded by triangles.
    """
    tiling = Tiling()
    triangle = tiling.add(
        Shape(3, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(3):
        triangle_2 = tiling.add_adjacent(triangle, i, 3)
        triangle_3 = tiling.add_adjacent(triangle_2, 0, 3)
        triangle_4 = tiling.add_adjacent(triangle_2, 2, 3)
        triangle_5 = tiling.add_adjacent(triangle_4, 2, 3)
    if repeated:
        pass
    return tiling

##############################################################################################
# List of the tilings in this module


TILINGS = [hexagon, octagon_square, dodecagon_hexagon_square, dodecagon_triangle,
           square, hexagon_square_triangle, hexagon_triangle, square_triangle,
           square_triangle_square, hexagon_triangle_triangle, triangle]

##############################################################################################
# If ran from the command line
if __name__ == "__main__":
    for tiling in TILINGS:
        system = System()
        tiling().add_to_system(system)
        system.render(plot, vertices=False, title=tiling.__name__)

##############################################################################################

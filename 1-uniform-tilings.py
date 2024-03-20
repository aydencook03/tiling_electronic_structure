from vec import Vec
from system import System
from tiling import Shape, Tiling
import matplotlib.pyplot as pyplot

##############################################################################################
# The Unit Pattern Generators for the 1-Uniform Tilings


def hexagon(tiling, side_length, pos, rotation, repeats):
    """
    A hexagon with a hexagon on each side.
    """
    hexagon = tiling.add(
        Shape(6, side_length=side_length, pos=pos, rotation=rotation))
    for i in range(6):
        hexagon_2 = tiling.add_adjacent(hexagon, i, 6)
        repeats.add(hexagon_2)


def octagon_square(tiling, side_length, pos, rotation, repeats):
    """
    An octagon with 4 surrounding squares.
    """
    octagon = tiling.add(
        Shape(8, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(4):
        square = tiling.add_adjacent(octagon, 2*i, 4)
        octagon_2 = tiling.add_adjacent(octagon, 2*i+1, 8)
        repeats.add(octagon_2)


def dodecagon_hexagon_square(tiling, side_length, pos, rotation, repeats):
    """
    A dodecagon surrounded by alternating hexagons and squares.
    """
    dodecagon = tiling.add(
        Shape(12, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(6):
        square = tiling.add_adjacent(dodecagon, 2*i, 4)
        hexagon = tiling.add_adjacent(dodecagon, 2*i+1, 6)
        repeats.add(square.adjacent(0, 12))


def dodecagon_triangle(tiling, side_length, pos, rotation, repeats):
    """
    A dodecagon surrounded by triangles and dodecagons.
    """
    dodecagon = tiling.add(
        Shape(12, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(6):
        triangle = tiling.add_adjacent(dodecagon, 2*i, 3)
        dodecagon_2 = tiling.add_adjacent(dodecagon, 2*i+1, 12)
        repeats.add(dodecagon_2)


def square(tiling, side_length, pos, rotation, repeats):
    """
    A square with a square on each side.
    """
    square = tiling.add(
        Shape(4, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(4):
        square_2 = tiling.add_adjacent(square, i, 4)
        square_3 = tiling.add_adjacent(square_2, 1, 4)
        repeats.add(square_2)


def hexagon_square_triangle(tiling, side_length, pos, rotation, repeats):
    """
    A hexagon with squares on each side. The squares have triangles on their sides.
    """
    hexagon = tiling.add(
        Shape(6, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(6):
        square = tiling.add_adjacent(hexagon, i, 4)
        triangle = tiling.add_adjacent(square, 1, 3)
        repeats.add(square.adjacent(0, 6))


def hexagon_triangle(tiling, side_length, pos, rotation, repeats):
    """
    A hexagon with a triangle on each side. Star of David.
    """
    hexagon = tiling.add(
        Shape(6, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(6):
        triangle = tiling.add_adjacent(hexagon, i, 3)
        hexagon_2 = tiling.add_adjacent(triangle, 0, 6)
        triangle_2 = tiling.add_adjacent(hexagon_2, 1, 3)
        repeats.add(hexagon_2)


def triangle_square(tiling, side_length, pos, rotation, repeats):
    """
    Alternating strips of triangles and squares.
    """
    triangle = tiling.add(
        Shape(3, pos=pos, rotation=rotation, side_length=side_length))
    
        

def square_triangle_square(tiling, side_length, pos, rotation, repeats):
    """
    Square surrounded by triangles that have squares on them.
    """
    square = tiling.add(
        Shape(4, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(4):
        triangle = tiling.add_adjacent(square, i, 3)
        square_2 = tiling.add_adjacent(triangle, 0, 4)
        triangle_2 = tiling.add_adjacent(triangle, 2, 3)


def hexagon_triangle_triangle(tiling, side_length, pos, rotation, repeats):
    """
    Hexagon surrounded by triangles that have triangles on them.
    """
    hexagon = tiling.add(
        Shape(6, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(6):
        triangle = tiling.add_adjacent(hexagon, i, 3)
        triangle_2 = tiling.add_adjacent(triangle, 0, 3)
        triangle_3 = tiling.add_adjacent(triangle, 2, 3)


def triangle(tiling, side_length, pos, rotation, repeats):
    """
    Triangle surrounded by triangles.
    """
    triangle = tiling.add(
        Shape(3, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(3):
        triangle_2 = tiling.add_adjacent(triangle, i, 3)
        triangle_3 = tiling.add_adjacent(triangle_2, 0, 3)
        triangle_4 = tiling.add_adjacent(triangle_2, 2, 3)
        triangle_5 = tiling.add_adjacent(triangle_4, 2, 3)
        repeats.add(triangle_3)
        repeats.add(triangle_4)

##############################################################################################
# List of the tiling units in this module


UNITS = [hexagon, octagon_square, dodecagon_hexagon_square, dodecagon_triangle,
         square, hexagon_square_triangle, hexagon_triangle, triangle_square,
         square_triangle_square, hexagon_triangle_triangle, triangle]

##############################################################################################
# Run this module from the command line to see the tilings


if __name__ == "__main__":
    for unit in UNITS:
        system = System()
        Tiling().add_unit_pattern(unit).add_to_system(system)
        system.render(pyplot, vertices=False, title=unit.__name__)

##############################################################################################

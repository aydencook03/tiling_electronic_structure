from tiling import Shape, Tiling

##############################################################################################
# The Unit Pattern Generators for the 1-Uniform Tilings


def hexagon(tiling, side_length, pos, rotation, repeats):
    """
    A hexagon with a hexagon on each side.
    """
    hexagon = tiling.add(
        Shape(6, side_length=side_length, pos=pos, rotation=rotation))
    for i in range(6):
        repeats.append(hexagon.adjacent(i, 6))


def octagon_square(tiling, side_length, pos, rotation, repeats):
    """
    An octagon with 4 surrounding squares.
    """
    octagon = tiling.add(
        Shape(8, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(4):
        square = tiling.add(octagon.adjacent(2*i, 4))
        repeats.append(tiling.add(octagon.adjacent(2*i+1, 8)))


def dodecagon_hexagon_square(tiling, side_length, pos, rotation, repeats):
    """
    A dodecagon surrounded by alternating hexagons and squares.
    """
    dodecagon = tiling.add(
        Shape(12, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(6):
        square = tiling.add(dodecagon.adjacent(2*i, 4))
        hexagon = tiling.add(dodecagon.adjacent(2*i+1, 6))
        repeats.append(square.adjacent(0, 12))


def dodecagon_triangle(tiling, side_length, pos, rotation, repeats):
    """
    A dodecagon surrounded by triangles and dodecagons.
    """
    dodecagon = tiling.add(
        Shape(12, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(6):
        triangle = tiling.add(dodecagon.adjacent(2*i, 3))
        repeats.append(tiling.add(dodecagon.adjacent(2*i+1, 12)))


def square(tiling, side_length, pos, rotation, repeats):
    """
    A square with a square on each side.
    """
    square = tiling.add(
        Shape(4, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(4):
        repeats.append(square.adjacent(i, 4))


def hexagon_square_triangle(tiling, side_length, pos, rotation, repeats):
    """
    A hexagon with squares on each side. The squares have triangles on their sides.
    """
    hexagon = tiling.add(
        Shape(6, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(6):
        square = tiling.add(hexagon.adjacent(i, 4))
        triangle = tiling.add(square.adjacent(1, 3))
        repeats.append(square.adjacent(0, 6))


def hexagon_triangle(tiling, side_length, pos, rotation, repeats):
    """
    A hexagon with a triangle on each side. Star of David.
    """
    hexagon = tiling.add(
        Shape(6, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(6):
        triangle = tiling.add(hexagon.adjacent(i, 3))
        repeats.append(tiling.add(triangle.adjacent(0, 6)))


def triangle_square(tiling, side_length, pos, rotation, repeats):
    """
    Alternating strips of triangles and squares.
    """
    square = tiling.add(
        Shape(4, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(2):
        square_2 = tiling.add(square.adjacent(i*2, 4))
        triangle = tiling.add(square.adjacent(i*2+1, 3))
        for j in range(2):
            triangle_2 = tiling.add(square_2.adjacent(j*2+1, 3))
            triangle_3 = tiling.add(triangle_2.adjacent(2*j, 3))
            repeats.append(triangle_3.adjacent((j+2) % 3, 4))
            # not needed, but looks nicer
            repeats.append(square_2.adjacent(0, 4))


def square_triangle_square(tiling, side_length, pos, rotation, repeats):
    """
    Square surrounded by triangles that have squares on them.
    """
    square = tiling.add(
        Shape(4, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(4):
        triangle = tiling.add(square.adjacent(i, 3))
        square_2 = tiling.add(triangle.adjacent(0, 4))
        triangle_2 = tiling.add(triangle.adjacent(2, 3))
        repeats.append(triangle_2.adjacent(0, 4))


def hexagon_triangle_triangle(tiling, side_length, pos, rotation, repeats):
    """
    Hexagon surrounded by triangles that have triangles on them.
    """
    hexagon = tiling.add(
        Shape(6, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(6):
        triangle = tiling.add(hexagon.adjacent(i, 3))
        triangle_2 = tiling.add(triangle.adjacent(0, 3))
        triangle_3 = tiling.add(triangle.adjacent(2, 3))
        repeats.append(triangle_2.adjacent(2, 6))


def triangle(tiling, side_length, pos, rotation, repeats):
    """
    Triangle surrounded by triangles.
    """
    triangle = tiling.add(
        Shape(3, pos=pos, rotation=rotation, side_length=side_length))
    for i in range(3):
        triangle_2 = tiling.add(triangle.adjacent(i, 3))
        repeats.append(triangle_2.adjacent(0, 3))
        # not needed, but looks nicer
        repeats.append(triangle_2.adjacent(2, 3))

##############################################################################################
# List of the unit tilings in this module


UNITS = [hexagon, octagon_square, dodecagon_hexagon_square, dodecagon_triangle,
         square, hexagon_square_triangle, hexagon_triangle, triangle_square,
         square_triangle_square, hexagon_triangle_triangle, triangle]

##############################################################################################
# Run this module from the command line to see the tilings


if __name__ == "__main__":
    import matplotlib.pyplot as pyplot
    for unit in UNITS:
        # Tiling().add_unit_pattern(unit, depth=4).render_full(pyplot, title=unit.__name__)
        Tiling().add_unit_pattern(unit).render_unit(pyplot, title="Unit: "+unit.__name__)

##############################################################################################

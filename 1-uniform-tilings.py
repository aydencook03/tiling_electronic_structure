from vec import Vec
from system import System
from tiling import Shape, Tiling
import matplotlib.pyplot as plot

##############################################################################################
# Make the tilings

tiling = Tiling()


hexagon = tiling.add(Shape(6, pos=Vec(-9, 9)))
# loop through all edges of the hexagon and add a hexagon to it
for i in range(6):
    hexagon_2 = tiling.add_adjacent(hexagon, i, 6)


octagon = tiling.add(Shape(8, pos=Vec(0, 9)))
for i in range(4):
    # add a square to every other side of the octagon
    square = tiling.add_adjacent(octagon, 2*i, 4)
    octagon_2 = tiling.add_adjacent(octagon, 2*i+1, 8)


dodecagon = tiling.add(Shape(12, pos=Vec(9, 9)))
for i in range(6):
    square = tiling.add_adjacent(dodecagon, 2*i, 4)
    hexagon = tiling.add_adjacent(dodecagon, 2*i+1, 6)


dodecagon = tiling.add(Shape(12, pos=Vec(-9, 0)))
for i in range(6):
    triangle = tiling.add_adjacent(dodecagon, 2*i, 3)
    dodecagon_2 = tiling.add_adjacent(dodecagon, 2*i+1, 12)


square = tiling.add(Shape(4, pos=Vec(0, 0)))
for i in range(4):
    square_2 = tiling.add_adjacent(square, i, 4)
    square_3 = tiling.add_adjacent(square_2, 1, 4)


hexagon = tiling.add(Shape(6, pos=Vec(9, 0)))
for i in range(6):
    square = tiling.add_adjacent(hexagon, i, 4)
    triangle = tiling.add_adjacent(square, 1, 3)


hexagon = tiling.add(Shape(6, pos=Vec(-9, -9)))
for i in range(6):
    triangle = tiling.add_adjacent(hexagon, i, 3)
    hexagon_2 = tiling.add_adjacent(triangle, 0, 6)
    triangle_2 = tiling.add_adjacent(hexagon_2, 1, 3)


square = tiling.add(Shape(4, pos=Vec(0, -9)))
for i in range(2):
    triangle = tiling.add_adjacent(square, 2*i, 3)
    square_2 = tiling.add_adjacent(square, 2*i+1, 4)
    triangle_2 = tiling.add_adjacent(square_2, 1, 3)
    triangle_3 = tiling.add_adjacent(square_2, 3, 3)
    triangle_4 = tiling.add_adjacent(triangle, 0, 3)
    triangle_5 = tiling.add_adjacent(triangle_2, 0, 3)


square = tiling.add(Shape(4, pos=Vec(9, -9)))
for i in range(4):
    triangle = tiling.add_adjacent(square, i, 3)
    square_2 = tiling.add_adjacent(triangle, 0, 4)
    triangle_2 = tiling.add_adjacent(triangle, 2, 3)


hexagon = tiling.add(Shape(6, pos=Vec(-9, -18)))
for i in range(6):
    triangle = tiling.add_adjacent(hexagon, i, 3)
    triangle_2 = tiling.add_adjacent(triangle, 0, 3)
    triangle_3 = tiling.add_adjacent(triangle, 2, 3)


triangle = tiling.add(Shape(3, pos=Vec(0, -18)))
for i in range(3):
    triangle_2 = tiling.add_adjacent(triangle, i, 3)
    triangle_3 = tiling.add_adjacent(triangle_2, 0, 3)
    triangle_4 = tiling.add_adjacent(triangle_2, 2, 3)
    triangle_5 = tiling.add_adjacent(triangle_4, 2, 3)

##############################################################################################
# If ran from the command line


if __name__ == "__main__":
    system = System()
    tiling.add_to_system(system)
    system.render(plot, vertices=False)

##############################################################################################

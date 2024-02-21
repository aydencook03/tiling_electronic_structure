from vec import Vec
from system import System
from tiling import Shape, Tiling
import matplotlib.pyplot as plot

###############################################

tiling = Tiling()

hexagon = tiling.add(Shape(6))
for i in range(6):
    square = tiling.add_adjacent(hexagon, i, 4)
    triangle = tiling.add_adjacent(square, 1, 3)

particles, links = tiling.to_system()

###############################################

system = System()
system.add_particles(particles)
system.add_links(links)

###############################################

system.render(plot, debug=True)

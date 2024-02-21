from vec import Vec
from system import System
from tiling import Shape, Tiling

import matplotlib.pyplot as plt

###############################################

tiling = Tiling(width=10, height=10, scale=10)
hexagon = tiling.add(Shape(5))
for i in range(5):
    square = tiling.add_adjacent(hexagon, i, 3)
    #triangle = tiling.add_adjacent(square, 3, 3)

particles, links = tiling.to_system()

###############################################

system = System()
system.add_particles(particles)
system.add_links(links)

###############################################

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

for particle in system.particles:
    pos = particle.pos
    ax.scatter(pos.x, pos.y, 0, color="black")

for link in system.links:
    x = [part.pos.x for part in link.particles]
    y = [part.pos.y for part in link.particles]
    z = [0, 0]
    ax.plot(x, y, z, color="black")

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_aspect("equal")

print(len(system.particles))
print(len(system.links))
plt.show()
from vec import Vec
from particle import Particle
from system import System

import matplotlib.pyplot as plt

from tile import Model, Shape

###############################################

model = Model(width=10, height=10, scale=10)

"""
center_triangle = model.append(Shape(3))
triangles = model.add(center_triangle, range(3), 3)
model.repeat(triangles)
"""


center_square = model.append(Shape(4))
squares = model.add(center_square, range(4), 4)
model.repeat(squares)


"""
center_hexagon = model.append(Shape(6))
squares = model.add(center_hexagon, range(6), 4)
triangles = model.add(squares, 1, 3)
hexagons = model.add(squares, 2, 6)
model.repeat(hexagons)
"""

vertices = model.particles()
edges = model.edges()

###############################################

system = System()
system.add_particles(vertices)

###############################################

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_aspect("equal")

for particle in system.particles:
    pos = particle.pos
    ax.scatter(pos.x, pos.y, pos.z, color="black")

for edge in edges:
    x = [edge[0][0], edge[1][0]]
    y = [edge[0][1], edge[1][1]]
    z = [0, 0]
    ax.plot(x, y, z, color="black")

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

print(len(system.particles))
print(len(edges))
plt.show()
from vec import Vec
from particle import Particle
from system import System
import tilings

import matplotlib.pyplot as plt

from tile import Model, Shape

###############################################

model = Model()
model.append(Shape(6))
a = model.add(0, range(6), 4)
b = model.add(a, 1, 3)
c = model.add(a, 2, 6)
model.repeat(c)
vertices = model.to_particles()

system = System()
#vertices, edges = tilings.square(Vec(0,0,0), 1, 5, 5)
system.add_particles(vertices)

###############################################

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

for particle in system.particles:
    pos = particle.pos
    ax.scatter(pos.x, pos.y, pos.z, color="black")

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
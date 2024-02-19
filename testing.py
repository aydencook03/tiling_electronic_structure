from vec import Vec
from particle import Particle
from system import System
import tilings

import matplotlib.pyplot as plt

###############################################

system = System()
vertices, edges = tilings.square(Vec(0,0,0), 1, 5, 5)
system.add_particles(vertices)

###############################################

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

for particle in system.particles:
    pos = particle.pos
    ax.scatter(pos.x, pos.y, pos.z, color="black")

for edge in edges:
    v_1 = edge.particles[0].pos
    v_2 = edge.particles[1].pos
    ax.plot([v_1.x, v_2.x], [v_1.y, v_2.y], [v_1.z, v_2.z], color="black")

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
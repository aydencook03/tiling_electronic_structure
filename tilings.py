from vec import Vec
from particle import Particle
from interaction import Link

def square(center, normal, edge_length, x_count, y_count):
    particles = [[Particle() for j in range(y_count)] for i in range(x_count)]
    links = []

    for i in range(x_count):
        for j in range(y_count):
            particles[i][j].pos = edge_length*Vec(i, j, 0) + center - edge_length*Vec(x_count-1, y_count-1, 0)/2

            if not i == 0:
                links.append(Link(particles[i][j], particles[i-1][j]))
            if not j == 0:
                links.append(Link(particles[i][j], particles[i][j-1]))

    return ([x for xs in particles for x in xs], links)
from vec import Vec

##############################################################################################


class Particle:
    def __init__(self, groups=set(), pos=Vec(0., 0.)):
        self.groups = groups
        self.pos = pos

    def __eq__(self, other):
        return isinstance(other, Particle) and self.pos == other.pos

    def __hash__(self):
        return hash(self.pos)

##############################################################################################


class Link:
    def __init__(self, particle_1, particle_2):
        self.particles = frozenset((particle_1, particle_2))

    def __eq__(self, other):
        return isinstance(other, Link) and self.particles == other.particles

    def __hash__(self):
        return hash(self.particles)

##############################################################################################


class System:
    def __init__(self):
        self.particles = set()
        self.links = set()

    def add_particles(self, particles):
        particle_iter = particles
        if not hasattr(particle_iter, "__iter__"):
            particle_iter = [particle_iter]
        for particle in particle_iter:
            self.particles.add(particle)
        return particles

    def add_links(self, links):
        links_iter = links
        if not hasattr(links_iter, "__iter__"):
            links_iter = [links_iter]
        for link in links_iter:
            self.links.add(link)
        return links

    def particles_in_group(self, group):
        particles = set()

        for particle in self.particles:
            if group in particle.groups:
                particles.add(particle)

        return particles

##############################################################################################

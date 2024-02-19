
class Interaction:
    def __init__(self, particles):
        self.particles = particles
    
    def handle(self, dt):
        pass

class Link(Interaction):
    def __init__(self, particle_1, particle_2):
        super().__init__((particle_1, particle_2))

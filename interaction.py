
class Interaction:
    def __init__(self, particles):
        self.particles = particles
    
    def handle(self, dt):
        pass

class Link(Interaction):
    def __init__(self, particle1, particle2):
        super().__init__((particle1, particle2))

from vec import Vec

class Particle:
    def __init__(self, id = 0, groups = {}, pos = Vec(0,0,0), vel = Vec(0,0,0), mass = 1.):
        # identity
        self.id = id
        self.groups = groups

        # state
        self.pos = pos
        self.vel = vel

        # dynamics
        self.mass = mass
        self.inverse_mass = 1./self.mass if self.mass != 0. else 0.
        self.prev_pos = self.pos
        self.forces = []

    def integrate(self, dt):
        total_force = Vec(0,0,0)

        for force in self.forces:
            total_force += force
        
        self.vel += total_force * self.inverse_mass * dt
        self.prev_pos = self.pos
        self.pos += self.vel * dt

    def add_force(self, force):
        self.forces.push(force)

    def clear_forces(self):
        self.forces.clear()

    def add_displacement(self, displacement, as_force = false, dt = 0.):
        if not as_force:
            self.pos += displacement
        else:
            self.add_force(self.mass * displacement / dt**2)

    def update_vel(self, dt):
        self.vel = (self.pos - self.prev_pos) / dt

class System:
    def __init__(self):
        self.time = 0.
        self.running = True
        self.substeps = 5

        self.particles = []
        #self.interactions
        #self.constraints

        self.id_counter = 0

    def add_particle(self, particle):
        particle.id = self.id_counter
        self.particles.append(particle)
        self.id_counter += 1

        return particle

    def add_particles(self, particles):
        for particle in particles:
            self.add_particle(particle)

        return particles

    #def add_interaction
    #def add_constraint

    def particles_in_group(self, group):
        particles = []

        for particle in self.particles:
            if group in particle.groups:
                particles.push(particle)

        return particles

    #def static_constraint_pass(self, iterations):

    def step_forward(self, dt):
        if not self.running or dt == 0.:
            return False
        
        sub_dt = dt / self.substeps

        for i in range(self.substeps):
            #handle interactions

            for particle in self.particles:
                particle.integrate(sub_dt)
                particle.forces.clear()

            #project constraints

            for particle in self.particles:
                particle.update_vel(sub_dt)

        self.time += dt
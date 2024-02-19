
class System:
    def __init__(self):
        self.time = 0.
        self.running = True
        self.substeps = 5

        self.particles = []
        self.interactions = []
        self.constraints = []

        self.id_counter = 0

    def add_particles(self, particles):
        particle_iter = particles

        if not hasattr(particle_iter, "__iter__"):
            particle_iter = [particle_iter]

        for particle in particle_iter:
            particle.id = self.id_counter
            self.particles.append(particle)
            self.id_counter += 1

        return particles

    def add_interactions(self, interactions):
        interaction_iter = interactions

        if not hasattr(interaction_iter, "__iter__"):
            interaction_iter = [interaction_iter]
        
        for interaction in interaction_iter:
            self.interactions.append(interaction)

        return interactions

    def add_constraints(self, constraints):
        constraint_iter = constraints

        if not hasattr(constraint_iter, "__iter__"):
            constraint_iter = [constraint_iter]
        
        for constraint in constraint_iter:
            self.constraints.append(constraint)

        return constraints

    def particles_in_group(self, group):
        particles = []

        for particle in self.particles:
            if group in particle.groups:
                particles.push(particle)

        return particles

    def static_constraint_pass(self, iterations):
        for i in range(iterations):
            for constraint in self.constraints:
                constraint.project(None, True)

    def step_forward(self, dt):
        if not self.running or dt == 0.:
            return False
        
        sub_dt = dt / self.substeps

        for i in range(self.substeps):
            for interaction in self.interactions:
                interaction.handle(sub_dt)

            for particle in self.particles:
                particle.integrate(sub_dt)
                particle.forces.clear()

            for constraint in self.constraints:
                constraint.project(sub_dt, False)

            for particle in self.particles:
                particle.update_vel(sub_dt)

        self.time += dt
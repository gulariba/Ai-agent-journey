import random  # Random numbers ke liye
import math    # Math functions ke liye (abhi directly use nahi kiya, but useful if needed)

# 🎯 Objective Function: jisko minimize karna hai
def objective_function(x, y):
    # Simple function: f(x, y) = x^2 + y^2
    return x**2 + y**2

# 🤖 Particle class: har particle ek AI agent jaisa hota hai
class Particle:
    def __init__(self):
        # Har particle ki random position: x, y [-10, 10] range mein
        self.position = [random.uniform(-10, 10), random.uniform(-10, 10)]

        # Initial velocity (random direction)
        self.velocity = [random.uniform(-1, 1), random.uniform(-1, 1)]

        # Apni best position (personal best)
        self.best_position = list(self.position)

        # Apni best value (objective function value at best position)
        self.best_value = objective_function(*self.position)

    # 🔄 Update velocity: particle kis direction mein move kare
    def update_velocity(self, global_best_position, w=0.5, c1=1.5, c2=1.5):
        # w = inertia, c1 = cognitive (self), c2 = social (swarm)
        for i in range(2):  # 2D (x, y)
            r1, r2 = random.random(), random.random()  # Random weights
            cognitive = c1 * r1 * (self.best_position[i] - self.position[i])  # Apne experience se seekhna
            social = c2 * r2 * (global_best_position[i] - self.position[i])   # Group ke best se seekhna
            self.velocity[i] = w * self.velocity[i] + cognitive + social  # Final velocity update

    # 📍 Update position: particle ko aage move karna
    def update_position(self):
        for i in range(2):  # x, y update
            self.position[i] += self.velocity[i]

        # Nayi position par objective function calculate karo
        value = objective_function(*self.position)

        # Agar nayi value purani best se achi hai to update best
        if value < self.best_value:
            self.best_value = value
            self.best_position = list(self.position)

# 🚀 PSO Main Function: pura swarm run karta hai yahan
def pso(num_particles=30, iterations=100):
    # N particles create karo
    swarm = [Particle() for _ in range(num_particles)]

    # Global best (poore swarm ka best start)
    global_best_position = swarm[0].best_position
    global_best_value = objective_function(*global_best_position)

    # Main loop: multiple iterations tak swarm move karta hai
    for _ in range(iterations):
        for particle in swarm:
            # Velocity update (based on personal + global best)
            particle.update_velocity(global_best_position)

            # Position update (move particle)
            particle.update_position()

            # Global best update agar koi aur aur behtar mila
            if particle.best_value < global_best_value:
                global_best_value = particle.best_value
                global_best_position = list(particle.best_position)

    # Final best position and value return karo
    return global_best_position, global_best_value

# 🧪 PSO Algorithm ko run karo
best_position, best_value = pso()

# ✅ Result print karo
print(f"Best Position: {best_position}")
print(f"Best Value: {best_value}")

#Ye code show karta hai kaise 30 agents (particles) milke ek optimization
#  problem ka solution dhoondte hain — bas apne aur team ke past experiences se.
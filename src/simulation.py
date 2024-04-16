import pygame
import random
import math
from sprites.particle import Particle


class Simulation:
    def __init__(self, particle_count, container):
        self.container = container
        self.particles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        for _ in range(particle_count):
            self.add_particle()
            
        self.all_sprites.add(self.container)

    def move_particles(self):
        thickness = self.container.thickness

        for particle in self.particles:
            particle.update()

            #generoitu koodi alkaa
            if particle.rect.left <= self.container.rect.left + thickness and particle.velocity[0] < 0:
                particle.velocity[0] *= -1
                particle.rect.left = self.container.rect.left + thickness
            elif particle.rect.right >= self.container.rect.right - thickness and particle.velocity[0] > 0:
                particle.velocity[0] *= -1
                particle.rect.right = self.container.rect.right - thickness

            if particle.rect.top <= self.container.rect.top + thickness and particle.velocity[1] < 0:
                particle.velocity[1] *= -1
                particle.rect.top = self.container.rect.top + thickness
            elif particle.rect.bottom >= self.container.rect.bottom - thickness and particle.velocity[1] > 0:
                particle.velocity[1] *= -1
                particle.rect.bottom = self.container.rect.bottom - thickness
            #generoitu koodi päättyy

    def update(self):
        self.move_particles()
        self.handle_collisions()
        self.all_sprites.update()

    #generoitu koodi alkaa
    def handle_collisions(self):
        for particle1 in self.particles:
            for particle2 in self.particles:
                if particle1 != particle2 and pygame.sprite.collide_circle(particle1, particle2):
                    # Calculate the direction vector
                    dx = particle1.x - particle2.x
                    dy = particle1.y - particle2.y
                    distance = math.sqrt(dx * dx + dy * dy)

                    # Normalize the direction vector
                    dx /= distance
                    dy /= distance

                    # Calculate the relative velocity
                    relative_velocity = [particle1.velocity[0] - particle2.velocity[0], particle1.velocity[1] - particle2.velocity[1]]

                    # Calculate the velocity along the direction vector
                    velocity_along_direction = relative_velocity[0] * dx + relative_velocity[1] * dy

                    # If the particles are moving away from each other, do nothing
                    if velocity_along_direction > 0:
                        continue

                    # Calculate the new velocities
                    impulse = 2 * velocity_along_direction / (particle1.mass + particle2.mass)
                    particle1.velocity[0] -= impulse * particle2.mass * dx
                    particle1.velocity[1] -= impulse * particle2.mass * dy
                    particle2.velocity[0] += impulse * particle1.mass * dx
                    particle2.velocity[1] += impulse * particle1.mass * dy
    #generoitu koodi päättyy

    def add_particle(self):
        red = (255, 0, 0)
        x = random.randint(150, 850)
        y = random.randint(150, 650)
        new_particle = Particle(red, 10, x, y, [random.uniform(-2,2), random.uniform(-2,2)])
        self.particles.add(new_particle)
        self.all_sprites.add(new_particle)




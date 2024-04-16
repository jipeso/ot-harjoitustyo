import math
import random
import pygame
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

            # generoitu koodi alkaa
            if particle.rect.left <= self.container.rect.left + thickness  \
                    and particle.velocity[0] < 0:
                particle.velocity[0] *= -1
                particle.rect.left = self.container.rect.left + thickness
            elif particle.rect.right >= self.container.rect.right - thickness \
                    and particle.velocity[0] > 0:
                particle.velocity[0] *= -1
                particle.rect.right = self.container.rect.right - thickness
            if particle.rect.top <= self.container.rect.top + thickness \
                    and particle.velocity[1] < 0:
                particle.velocity[1] *= -1
                particle.rect.top = self.container.rect.top + thickness
            elif particle.rect.bottom >= self.container.rect.bottom - thickness \
                    and particle.velocity[1] > 0:
                particle.velocity[1] *= -1
                particle.rect.bottom = self.container.rect.bottom - thickness
            # generoitu koodi päättyy

    def update(self):
        self.move_particles()
        self.handle_collisions()
        self.all_sprites.update()

    def handle_collisions(self):

        # generoitu koodi alkaa
        for particle1 in self.particles:
            for particle2 in self.particles:
                if particle1 == particle2 or not pygame.sprite.collide_circle(particle1, particle2):
                    continue
                # Laske suuntavektori
                _dx = particle1.x_coord - particle2.x_coord
                _dy = particle1.y_coord - particle2.y_coord
                distance = math.sqrt(_dx * _dx + _dy * _dy)

                # Normalisoi suuntavektori
                _dx /= distance
                _dy /= distance

                # Laske suhteellinen nopeus
                relative_velocity = [particle1.velocity[0] - particle2.velocity[0],
                                     particle1.velocity[1] - particle2.velocity[1]]

                # Laske nopeus suuntavektorin suuntaisesti
                velocity_along_direction = relative_velocity[0] * \
                    _dx + relative_velocity[1] * _dy

                if velocity_along_direction > 0:
                    continue

                # Uudet nopeudet
                impulse = 2 * velocity_along_direction / \
                    (particle1.mass + particle2.mass)
                particle1.velocity[0] -= impulse * particle2.mass * _dx
                particle1.velocity[1] -= impulse * particle2.mass * _dy
                particle2.velocity[0] += impulse * particle1.mass * _dx
                particle2.velocity[1] += impulse * particle1.mass * _dy
        # generoitu koodi päättyy

    def add_particle(self):
        red = (255, 0, 0)
        _x = random.randint(150, 850)
        _y = random.randint(150, 650)
        new_particle = Particle(
            red, 10, _x, _y, [random.uniform(-2, 2), random.uniform(-2, 2)])
        self.particles.add(new_particle)
        self.all_sprites.add(new_particle)

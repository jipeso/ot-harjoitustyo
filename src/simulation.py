import pygame
from sprites.particle import Particle
from sprites.container import Container


class Simulation:
    def __init__(self, display, particles, container):
        self.container = pygame.sprite.Group(container)
        self.particles = pygame.sprite.Group(particles)
        self.all_sprites = pygame.sprite.Group()

        self.all_sprites.add(self.particles)
        self.all_sprites.add(self.container)

    def move_particles(self):
        container = next(iter(self.container))
        thickness = container.thickness
        for particle in self.particles:
            particle.update()

            if particle.rect.left <= container.rect.left + thickness or particle.rect.right >= container.rect.right - thickness:
                particle.velocity[0] *= -1
            if particle.rect.top <= container.rect.top + thickness or particle.rect.bottom >= container.rect.bottom - thickness:
                particle.velocity[1] *= -1

    def update(self):
        self.move_particles()
        self.all_sprites.update()





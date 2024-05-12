import random
import math

import pygame
import pymunk
from sprites.particle import Particle
from sprites.segment import Segment


class Collisions:
    def __init__(self):
        self._display = pygame.display.get_surface()
        self._display_width = self._display.get_width()
        self._display_height = self._display.get_height()
        self._mouse_pos = None
        self._fps = 60

        self._clock = pygame.time.Clock()

        self.space = pymunk.Space()
        self.space.gravity = (0, 0)

        self.static_elements = []
        self.particle_list = []

        self.create_static_elements()


    def create_static_elements(self):
        border_edges = [
            (0, 0),
            (self._display_width, 0),
            (self._display_width, self._display_height),
            (0, self._display_height)
        ]

        for i in range(len(border_edges)):
            new_segmment = Segment(
                start=border_edges[i-1],
                end=border_edges[i],
                radius=30,
                color=(211, 211, 211),
                elasticity=1,
                friction=0,
                body_type=pymunk.Body.STATIC
            )
            self.static_elements.append(new_segmment)
            self.space.add(new_segmment.body, new_segmment.shape)

    def create_new_particle(self, center):

        color = random.choices(range(256), k=3)
        angle = random.uniform(0, 2 * math.pi)
        velocity = [300 * math.cos(angle), 300 * math.sin(angle)]

        new_particle = Particle(
            mass = 1,
            moment = 1,
            center = center,
            velocity = velocity,
            color = color,
            radius = 15,
            elasticity = 1,
            friction = 0
        )

        self.particle_list.append(new_particle)
        self.space.add(new_particle.body, new_particle.shape)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._mouse_pos = pygame.mouse.get_pos()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    for particle in self.particle_list:
                        self.space.remove(particle.body, particle.shape)
                    self.particle_list.clear()

            elif event.type == pygame.QUIT:
                return False

        return True

    def run_simulation(self):
        self.space.step(1/self._fps)

        for particle in self.particle_list:
            if particle.out_of_bounds(self._display_width, self._display_height):
                self.space.remove(particle.body, particle.shape)
                self.particle_list.remove(particle)

        if self._mouse_pos:
            self.create_new_particle(self._mouse_pos)
            self._mouse_pos = None

        pygame.display.set_caption(
            f"Particle count: {len(self.particle_list)} \
            (Click to add a particle or press 'f' to reset)"
            )

    def render(self):
        self._display.fill((0, 0, 0))

        for particle in self.particle_list:
            particle.draw(self._display)

        for element in self.static_elements:
            element.draw(self._display)

        pygame.display.update()

    def clock_tick(self):
        self._clock.tick(self._fps)

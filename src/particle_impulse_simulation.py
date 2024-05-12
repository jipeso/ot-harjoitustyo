import math

import pygame
import pymunk

from sprites.particle import Particle
from sprites.segment import Segment

class ParticleImpulse:
    def __init__(self):
        self._display = pygame.display.get_surface()
        self._display_width = self._display.get_width()
        self._display_height = self._display.get_height()
        self._fps = 60
        self._clock = pygame.time.Clock()
        self.space = pymunk.Space()
        self.attempts_counter = 0
        self.start_pos = (95 , self._display_height - 75)
        self.particle = None

        self.space.gravity = (0, 400)
        self.space.damping = 0.6

        self.static_elements = []
        self.particle_list = []
        self.targets_list = []
        self.mouse_pressed = False
        self.mouse_pressed_pos = None
        self.mouse_released_pos = None

        self.create_static_elements()
        self.restart()

    def create_static_elements(self):
        platforms = []
        edges = [
            (0, self._display_height),
            (0, 0),
            (self._display_width, 0),
            (self._display_width, self._display_height)
        ]

        for i in range(1, len(edges)):
            new_segmment = Segment(
                start=edges[i - 1],
                end=edges[i],
                radius=30,
                color=(211, 211, 211),
                elasticity=0.8,
                friction=0.6,
                body_type=pymunk.Body.STATIC
            )
            self.static_elements.append(new_segmment)
            self.space.add(new_segmment.body, new_segmment.shape)

        start_platform = Segment(
            start=(80, self._display_height - 60),
            end=(110, self._display_height - 60),
            radius=10,
            color=(211, 211, 211),
            elasticity=0.6,
            friction=0.8,
            body_type=pymunk.Body.STATIC
        )

        platform1 = Segment(
            start=(self._display_width // 2 + 195, self._display_height - 60),
            end=(self._display_width - 205, self._display_height - 60),
            radius=10,
            color=(211, 211, 211),
            elasticity=0.6,
            friction=0.8,
            body_type=pymunk.Body.STATIC
        )

        obstacle =  Segment(
            start=(self._display_width // 2, 300),
            end=(self._display_width // 2, self._display_height),
            radius=10,
            color=(211, 211, 211),
            elasticity=1,
            friction=0,
            body_type=pymunk.Body.STATIC
        )

        platforms.append(start_platform)
        platforms.append(platform1)
        platforms.append(obstacle)

        for platform in platforms:
            self.static_elements.append(platform)
            self.space.add(platform.body, platform.shape)


    def create_new_particle(self, center, color=(255, 0, 0)):

        new_particle = Particle(
            mass = 1,
            moment = 1,
            center = center,
            velocity = (0, 0),
            color = color,
            radius = 15,
            elasticity = 0.6,
            friction = 0.6
        )

        self.particle_list.append(new_particle)
        self.space.add(new_particle.body, new_particle.shape)

        return new_particle

    def restart(self):
        self.attempts_counter = 0
        if self.particle_list:
            for particle in self.particle_list:
                self.space.remove(particle.body, particle.shape)
            self.particle_list.clear()
            self.targets_list.clear()

        self.particle = self.create_new_particle(self.start_pos, (0, 255, 0))

        targets = [
        self.create_new_particle((self._display_width - 285, self._display_height - 75)),
        self.create_new_particle((self._display_width - 255, self._display_height - 75)),
        self.create_new_particle((self._display_width - 225, self._display_height - 75)),
        self.create_new_particle((self._display_width - 285, self._display_height - 95)),
        self.create_new_particle((self._display_width - 255, self._display_height - 95)),
        self.create_new_particle((self._display_width - 225, self._display_height - 95)),
        self.create_new_particle((self._display_width - 285, self._display_height - 125)),
        self.create_new_particle((self._display_width - 255, self._display_height - 125)),
        self.create_new_particle((self._display_width - 225, self._display_height - 125))
        ]

        for target in targets:
            self.targets_list.append(target)

        pygame.display.set_caption(
                f"Attempts: {self.attempts_counter} (Click to apply impulse or press f to reset)"
            )

    def handle_events(self):
        for event in pygame.event.get():
            if self.particle.body.velocity == (0, 0):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_pressed = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_pressed = False
                    self.mouse_released_pos = pygame.mouse.get_pos()
                    self.launch_particle()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    self.restart()

            elif event.type == pygame.QUIT:
                return False

        return True

    def calc_distance(self, a, b):
        x1, y1 = a
        x2, y2 = b
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def calc_angle(self, a, b):
        x1, y1 = a
        x2, y2 = b
        angle = math.atan2(y2 - y1, x2 - x1)
        return angle

    def launch_particle(self):
        if self.mouse_released_pos:
            impulse = self.calc_distance(self.particle.body.position, self.mouse_released_pos) * 2
            angle = self.calc_angle(self.particle.body.position, self.mouse_released_pos)
            fx = math.cos(angle) * impulse
            fy = math.sin(angle) * impulse
            self.particle.body.apply_impulse_at_local_point((fx, fy), (0, 0))
            self.mouse_pressed_pos = None
            self.mouse_released_pos = None
            self.attempts_counter += 1
            pygame.display.set_caption(
                f"Attempts: {self.attempts_counter} (Click to apply impulse or press f to reset)"
            )

    def run_simulation(self):
        self.space.step(1/self._fps)

        if len(self.targets_list) == 0:
            pygame.display.set_caption(
                f"You completed the challenge in {self.attempts_counter} attempts!"
            )
            pygame.time.wait(4000)
            self.restart()

        if self.particle.out_of_bounds(self._display_width, self._display_height):
            self.space.remove(self.particle.body, self.particle.shape)
            self.particle_list.remove(self.particle)
            self.particle = self.create_new_particle(self.start_pos, (0, 255, 0))

        for particle in self.particle_list:
            if particle.body.velocity.length < 1:
                particle.body.velocity = (0, 0)
                particle.body.angular_velocity = 0

        for target in self.targets_list:
            if target.out_of_bounds(self._display_width, self._display_height):
                self.space.remove(target.body, target.shape)
                self.particle_list.remove(target)
                self.targets_list.remove(target)

    def render(self):
        self._display.fill((0, 0, 0))

        for particle in self.particle_list:
            particle.draw(self._display)

        for element in self.static_elements:
            element.draw(self._display)

        if self.mouse_pressed:
            pygame.draw.line(
                self._display,
                (211, 211, 211),
                self.particle.body.position,
                pygame.mouse.get_pos(),
                3
            )

        pygame.display.update()

    def clock_tick(self):
        self._clock.tick(self._fps)

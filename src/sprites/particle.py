import pygame
import pymunk

class Particle:
    def __init__(
            self,
            mass,
            moment,
            center,
            velocity,
            color,
            radius,
            elasticity,
            friction,
        ):

        self.body = pymunk.Body(mass=mass, moment=moment, body_type=pymunk.Body.DYNAMIC)
        self.body.position = center
        self.body.velocity = velocity
        self.color = color
        self.radius = radius
        self.shape = pymunk.Circle(body=self.body, radius=self.radius)
        self.shape.elasticity = elasticity
        self.shape.friction = friction

    def out_of_bounds(self, display_width, display_height):
        x, y = self.body.position
        return x + self.radius // 2 > display_width or x - self.radius // 2 < 0 \
            or y + self.radius // 2 > display_height or y - self.radius // 2 < 0


    def draw(self, display):

        pygame.draw.circle(
            surface=display,
            color=self.color,
            center=self.body.position,
            radius=self.radius
        )

import pygame
import pymunk

class Segment:
    def __init__(self, start, end, radius, color, elasticity, friction, body_type):
        self.start = start
        self.end = end
        self.radius = radius
        self.color = color
        self.elasticity = elasticity
        self.friction = friction
        self.body_type = body_type

        self.body = pymunk.Body(body_type=self.body_type)
        self.shape = pymunk.Segment(self.body, self.start, self.end, self.radius)
        self.shape.elasticity = elasticity
        self.shape.friction = friction

    def draw(self, display):
        pygame.draw.line(
            display,
            self.color,
            self.start,
            self.end,
            self.radius * 2
        )

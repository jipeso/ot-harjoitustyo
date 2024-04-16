import pygame

class Particle(pygame.sprite.Sprite):
    def __init__(self, color, radius, x, y, velocity, mass=1):
        super().__init__()
        self.color = color
        self.radius = radius
        self.x = x
        self.y = y
        self.velocity = velocity
        self.mass = mass

        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)

        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        self.rect.center = (self.x, self.y)

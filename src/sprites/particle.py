import pygame


class Particle(pygame.sprite.Sprite):
    def __init__(self, color, radius, x_coord, y_coord, velocity, mass=1):
        super().__init__()
        self.color = color
        self.radius = radius
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.velocity = velocity
        self.mass = mass

        self.image = pygame.Surface((radius * 2, radius * 2))
        pygame.draw.circle(self.image, color, (radius, radius), radius)

        self.rect = self.image.get_rect(center=(x_coord, y_coord))

    def update(self):
        self.x_coord += self.velocity[0]
        self.y_coord += self.velocity[1]

        self.rect.center = (self.x_coord, self.y_coord)

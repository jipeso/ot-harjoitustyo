import pygame

class Container(pygame.sprite.Sprite):
    def __init__(self, width, height, thickness=100):
        super().__init__()
        self.thickness = thickness

        #generoitu koodi alkaa
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)

        pygame.draw.rect(self.image, (0, 0, 255), pygame.Rect(0, 0, width, thickness))  # Top edge
        pygame.draw.rect(self.image, (0, 0, 255), pygame.Rect(0, height - thickness, width, thickness))  # Bottom edge
        pygame.draw.rect(self.image, (0, 0, 255), pygame.Rect(0, 0, thickness, height))  # Left edge
        pygame.draw.rect(self.image, (0, 0, 255), pygame.Rect(width - thickness, 0, thickness, height))  # Right edge
        #generoitu koodi päättyy

        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)

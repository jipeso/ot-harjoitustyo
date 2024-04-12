import pygame

class Renderer:
    def __init__(self, display, simulation):
        self._display = display
        self._simulation = simulation
        
    def render(self):
        self._display.fill((0, 0, 0)) 
        self._simulation.all_sprites.draw(self._display)
        pygame.display.update()
import pygame

class GameLoop:
    def __init__(self, simulation, renderer, event_queue, clock):
        self._simulation = simulation
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock

    def start(self):
        while True:
            if self.handle_events() == False:
                break

            self._simulation.update()
            self._render()
            self._clock.tick(60)

    def handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False

    def _render(self):
        self._renderer.render()
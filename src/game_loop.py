import pygame


class GameLoop:
    def __init__(self, simulation, renderer, event_queue, clock):
        self._simulation = simulation
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            if self.handle_events() is False:
                break

            self._simulation.update()
            self._render()
            self._clock.tick(60)

    def stop(self):
        self.running = False

    def handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self._simulation.add_particle()
        return True

    def _render(self):
        self._renderer.render()

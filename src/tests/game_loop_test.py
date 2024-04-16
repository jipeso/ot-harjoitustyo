import unittest
import pygame

from simulation import Simulation
from game_loop import GameLoop
from sprites.container import Container


class StubEvent:
    def __init__(self, type, key):
        self.type = type
        self.key = key


class StubEventQueue():
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events


class StubRenderer:
    def render(self):
        pass


class StubClock:
    def tick(self, fps):
        pass

    def get_ticks(self):
        return 0


SIMULATION_PARTICLES = 10
display_width = 1000
display_height = 800
container = Container(display_width, display_height)


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.simulation = Simulation(SIMULATION_PARTICLES, container)

    def test_can_simulate(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_SPACE),
                  StubEvent(pygame.QUIT, None)]

        game_loop = GameLoop(self.simulation, StubRenderer(),
                             StubEventQueue(events), StubClock())

        game_loop.start()

        self.assertTrue(game_loop.running)

import pygame
from game_loop import GameLoop
from event_queue import EventQueue
from renderer import Renderer
from clock import Clock
from simulation import Simulation
from sprites.container import Container
from sprites.particle import Particle


def main():
    display_width = 1000
    display_height = 800
    red = (255, 0, 0)

    display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Physics Simulator")
    
    container = Container(display_width, display_height)
    particle = Particle(red, 10, 400, 400, [2,2])
    event_queue = EventQueue()
    simulation = Simulation(display, particle, container)
    renderer = Renderer(display, simulation)
    clock = Clock()
    game_loop = GameLoop(simulation, renderer, event_queue, clock)


    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()



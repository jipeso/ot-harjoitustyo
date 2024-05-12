import pygame
import pygame_menu

from particles_colliding_simulation import Collisions
from particles_with_gravity_simulation import GravityCollisions
from particle_impulse_simulation import ParticleImpulse


def main():
    display_width = 1000
    display_height = 800

    pygame.init()
    display = pygame.display.set_mode((display_width, display_height))
    select_simulation_menu = create_select_menu(display_width, display_height)

    while True:
        if select_simulation_menu.is_enabled():
            handle_events()
            select_simulation_menu.mainloop(display)

def create_select_menu(display_width, display_height):
    pygame.display.set_caption("Physics Simulations")

    select_simulation_menu = pygame_menu.Menu(
        height=display_height * 0.7,
        width=display_width * 0.7,
        theme=pygame_menu.themes.THEME_DARK,
        title="Select a simulation",
    )

    select_simulation_menu.add.button("Collisions", start_collisions)
    select_simulation_menu.add.button("Collisions with Gravity", start_gravity_collisions)
    select_simulation_menu.add.button("Impulse to particle", start_particle_impulse)
    return select_simulation_menu

def start_collisions():
    collision_simulation = Collisions()

    running = True
    while running:
        running = collision_simulation.handle_events()
        collision_simulation.run_simulation()
        collision_simulation.render()
        collision_simulation.clock_tick()

    pygame.display.set_caption("Physics Simulations")

def start_gravity_collisions():
    gravity_simulation = GravityCollisions()

    running = True
    while running:
        running = gravity_simulation.handle_events()
        gravity_simulation.run_simulation()
        gravity_simulation.render()
        gravity_simulation.clock_tick()

    pygame.display.set_caption("Physics Simulations")

def start_particle_impulse():
    impulse_simulation = ParticleImpulse()

    running = True
    while running:
        running = impulse_simulation.handle_events()
        impulse_simulation.run_simulation()
        impulse_simulation.render()
        impulse_simulation.clock_tick()

    pygame.display.set_caption("Physics Simulations")

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

if __name__ == "__main__":
    main()

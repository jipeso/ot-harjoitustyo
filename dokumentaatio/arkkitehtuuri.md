```mermaid
classDiagram
    GameLoop "1" -- "1" Simulation
    EventQueue "1" -- "1" GameLoop
    Particle "*" -- "1" Simulation

    class Simulation{
        update()
        move_particles()
        handle_collisions()
    }
    class Particle{
        x
        y
        velocity
    }
    class GameLoop{
        start()
        handle_events()
    }
    class EventQueue{
        get()
    }
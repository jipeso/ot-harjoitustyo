```mermaid
classDiagram
    Particle "*" -- "1" Simulation
    Segment "*" -- "1" Simulation

    class Simulation{
        run_simulation()
        render()
        handle_events()
        create_particle()
        create_segment()
    }
    class Particle{
        mass
        moment
        velocity
        radius
        elasticity
        friction
    }
    class Segment{
        start
        end
        radius
    }
import unittest

import pymunk

from sprites.particle import Particle
from sprites.segment import Segment


class TestSprite(unittest.TestCase):

    def test_particle(self):
        particle = Particle(
            mass=1,
            moment=1,
            center=(500, 500),
            velocity=(0, 0),
            color=(255, 0, 0),
            radius=10,
            elasticity=1,
            friction=1
        )
        self.assertEqual(particle.body.mass, 1)
        self.assertEqual(particle.body.moment, 1)
        self.assertEqual(particle.body.position, (500, 500))
        self.assertEqual(particle.body.velocity, (0, 0))
        self.assertEqual(particle.color, (255, 0, 0))
        self.assertEqual(particle.radius, 10)
        self.assertEqual(particle.shape.elasticity, 1)
        self.assertEqual(particle.shape.friction, 1)

    def test_segment(self):
        segment = Segment(
            start=(0, 0),
            end=(100, 100),
            radius=10,
            color=(0, 0, 0),
            elasticity=1,
            friction=1,
            body_type=pymunk.Body.STATIC
        )

        self.assertEqual(segment.start, (0, 0))
        self.assertEqual(segment.end, (100, 100))
        self.assertEqual(segment.radius, 10)
        self.assertEqual(segment.color, (0, 0, 0))
        self.assertEqual(segment.shape.elasticity, 1)
        self.assertEqual(segment.shape.friction, 1)
        self.assertEqual(segment.body.body_type, pymunk.Body.STATIC)


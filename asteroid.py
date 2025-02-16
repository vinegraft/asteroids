import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def draw(self):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self):
        self.position += super().velocity * dt

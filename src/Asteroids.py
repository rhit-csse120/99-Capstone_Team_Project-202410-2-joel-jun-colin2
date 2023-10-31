import pygame
import random
from Asteroid import Asteroid

class Asteroids:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

        self.list_of_asteroids = []
        for k in range(10):
            self.list_of_asteroids.append(Asteroid(screen))

    def draw(self):
        pass
    def move(self):
        pass


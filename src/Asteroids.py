import pygame
import random
from Asteroid import Asteroid


class Asteroids:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

        self.list_of_asteroids = []
        for k in range(random.randint(9, 14)):
            self.list_of_asteroids.append(Asteroid(screen))

    def draw(self):
        for asteroid in self.list_of_asteroids:
            asteroid.draw()

    def move(self):
        for asteroid in self.list_of_asteroids:
            asteroid.move()

    def remove_asteroid(self):
        for k in range(len(self.list_of_asteroids) - 1, -1, -1):
            asteroid = self.list_of_asteroids[k]
            if asteroid.off_screen:
                del self.list_of_asteroids[k]
                self.list_of_asteroids.append(Asteroid(self.screen))

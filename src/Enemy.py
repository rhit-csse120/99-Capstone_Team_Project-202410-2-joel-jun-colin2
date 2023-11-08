import pygame
import random
from Starship import Ship
class Enemy:
    def __init__(self, screen: pygame.Surface, ship: Ship):
        self.screen = screen
        self.image = pygame.image.load("../media/Asteroid_S.gif")
        self.x = screen.get_width()
        self.ship = ship
        self.y = 100
        self.spawn_rate = random.randint(0, 1000000)

    def draw(self):
        if self.spawn_rate == 1:
            self.screen.blit(self.image, (self.x - 50, self.y))
            print(self.spawn_rate)
        else:
            self.spawn_rate = random.randint(0, 50)
            print(self.spawn_rate)
    def move(self):
        if self.spawn_rate == 1:
            self.x += -7
            self.y = self.ship.y




import pygame
import random
from Starship import Ship
import time
class Enemy:
    def __init__(self, screen: pygame.Surface, ship: Ship):
        self.screen = screen
        self.image = pygame.image.load("../media/Asteroid_S.gif")
        self.x = screen.get_width()
        self.ship = ship
        self.y = 100
        self.x_speed = 7
        self.stored_time = time.time()
        self.spawn_time = 20
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))


    def move(self):
        pass
    #     if time.time() >=
    #         self.x -= self.x_speed
    #         if self.y < self.ship.y:
    #             self.y += 2.5
    #         if self.y > self.ship.y:
    #             self.y -= 2.5
    #         if self.x < -100:
    #             self.x = 1300





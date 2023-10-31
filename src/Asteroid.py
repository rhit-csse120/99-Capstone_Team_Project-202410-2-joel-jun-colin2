import pygame
import random

class Asteroid:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.speed = random.randint(1, 10)
        self.image = pygame.image.load("../media/Asteroid_S.gif")
        self.x = screen.get_width() - 100
        self.y = random.randint(0, screen.get_height())
        self.off_screen = False

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x = self.x - self.speed

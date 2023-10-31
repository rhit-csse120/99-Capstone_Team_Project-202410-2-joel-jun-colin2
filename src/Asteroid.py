import pygame

class Asteroid:
    def __init__(self, screen: pygame.Surface, y, speed):
        self.screen = screen
        self.speed = speed
        self.image = pygame.image.load("../media/Asteroid_S.gif")
        self.x = screen.get_width() - 100
        self.y = y

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        pass
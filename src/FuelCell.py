import pygame
class FuelCell:
    def __init__(self, screen, x, y, height, width):
        self.screen = screen
        self.image = pygame.image.load()
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))


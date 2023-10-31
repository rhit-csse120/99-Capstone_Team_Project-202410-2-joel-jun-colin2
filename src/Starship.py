# author: Joel

import pygame


class Ship:

    def __init__(self, screen: pygame.Surface, speed=5):
        self.screen = screen
        self.image = pygame.image.load("../media/Starship.gif")
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # Ship rendered at center of left side of screen
        self.x = 100
        self.y = self.screen.get_height() // 2

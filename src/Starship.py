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

        self.speed = speed
        self.has_exploded = False

    def draw_self(self):
        self.screen.blit(self.image,(self.x,self.y))

    def move_left(self):
        if self.x > self.image.get_width() // 2:
            self.x -= self.speed

    def move_right(self):
        if self.x < self.screen.get_width() - (self.image.get_width() // 2):
            self.x += self.speed

    def move_up(self):
        if self.y > self.image.get_height() // 2:
            self.y -= self.speed

    def move_down(self):
        if self.y < self.screen.get_height() - (self.image.get_height() // 2):
            self.y += self.speed

    def is_hit_by(self):
        pass

    def explode(self):
        pass

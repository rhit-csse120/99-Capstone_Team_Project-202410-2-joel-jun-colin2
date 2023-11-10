# author: Joel

import pygame
from Asteroid import Asteroid

class Ship:

    def __init__(self, screen: pygame.Surface, speed=5):
        self.screen = screen
        self.image = pygame.image.load("../media/Starship.png")
        size = (125, 50)
        self.image = pygame.transform.scale(self.image, size)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # Ship rendered at center of left side of screen
        self.x = 100
        self.y = self.screen.get_height() // 2

        self.speed = speed
        self.explosion_sound = pygame.mixer.Sound("../media/explosion.wav")
        self.has_exploded = False

    def draw_self(self):
        self.screen.blit(self.image,(self.x,self.y))

    def move_left(self):
        if self.x > 0:
            self.x -= self.speed

    def move_right(self):
        if self.x < self.screen.get_width() - self.image.get_width():
            self.x += self.speed

    def move_up(self):
        if self.y > 0:
            self.y -= self.speed

    def move_down(self):
        if self.y < self.screen.get_height() - self.image.get_height():
            self.y += self.speed

    def is_hit_by(self, list_asteroids, jun):
        # Function will return True if an asteroid and the ship's rectangle collide
        ship_rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        for i in range(len(list_asteroids)):
            asteroid_rect = pygame.Rect(list_asteroids[i].x, list_asteroids[i].y,
                                    list_asteroids[i].image.get_width(), list_asteroids[i].image.get_height())
            if ship_rect.colliderect(asteroid_rect):
                self.has_exploded = True
                return True
        jun_rect = pygame.Rect(jun.x, jun.y, jun.image.get_width(), jun.image.get_height())
        if ship_rect.colliderect(jun_rect):
            self.has_exploded = True
            return True

    def explode(self):
        # Game over
        self.explosion_sound.play()
        self.has_exploded = True

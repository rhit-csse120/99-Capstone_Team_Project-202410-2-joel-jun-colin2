import pygame
from Starship import Ship
import random

class FuelCell:
    def __init__(self, screen, speed):
        self.screen = screen
        self.image = pygame.image.load("../media/fuelcell1.png")
        size = (40, 60)
        self.image = pygame.transform.scale(self.image, size)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = random.randint(screen.get_width(), screen.get_width() + 500)
        self.y = random.randint(0, screen.get_height() - 100)
        self.speed = speed
        self.is_off_the_screen = False
        self.has_consumed = False
        self.has_charged = False
        self.score = 100
        self.time = pygame.time.Clock()
        self.charge_sound = pygame.mixer.Sound("../media/pickup.mp3")

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def is_consumed(self, starship: Ship):
        fuel_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        starship_rect = pygame.Rect(starship.x, starship.y, starship.width, starship.height)
        if fuel_rect.colliderect(starship_rect):
            self.has_consumed = True
            self.charge_sound.play()

    def move(self):
        self.x -= self.speed
        if self.x < -10:
            self.is_off_the_screen = True







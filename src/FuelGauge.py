import pygame
from FuelCells import FuelCells
from Starship import Ship


class FuelGauge:
    def __init__(self, screen):
        self.x = screen.get_width()
        self.y = screen.get_height()
        self.ship = Ship(screen)
        self.screen = screen
        self.fuelCells_list = FuelCells(screen, self.ship)
        self.fuel_level = self.fuelCells_list.health
        self.font = pygame.font.Font('freesansbold.ttf', 50)
        self.font2 = pygame.font.Font('freesansbold.ttf', 50)
        self.text = self.font.render('Gauge', True, (0, 255, 0, 255), (0, 0, 255, 255))
        self.text2 = self.font2.render(str(self.fuel_level), True, (0, 255, 0, 255), (0, 0, 255, 255))
        self.textRect = self.text.get_rect()
        self.textRect2 = self.text2.get_rect()
        self.textRect.center = (self.screen.get_width() // 2, 35)
        self.textRect2.center = (self.screen.get_width() // 2, 88)

    def draw(self):
        self.screen.blit(self.text, self.textRect)
        self.screen.blit(self.text2, self.textRect2)

    def update_fuel_level(self):
        self.fuelCells_list.update_health()

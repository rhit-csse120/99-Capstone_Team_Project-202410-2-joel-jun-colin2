import pygame
from FuelCells import FuelCells
from Starship import Ship
import time


class FuelGauge:
    def __init__(self, screen, fuel_cells):
        self.x = screen.get_width()
        self.y = screen.get_height()
        self.clock = pygame.time.Clock()
        self.time = self.clock.get_time()
        self.ship = Ship(screen)
        self.screen = screen
        self.fuelCells_list = fuel_cells
        self.fuel_level = self.fuelCells_list.health
        self.fuel_level = round(self.fuel_level)
        self.font = pygame.font.Font('freesansbold.ttf', 50)
        self.font2 = pygame.font.Font('freesansbold.ttf', 50)
        self.font3 = pygame.font.Font('freesansbold.ttf', 50)
        self.text = self.font.render('Gauge', True, (0, 255, 0, 255), (0, 0, 255, 255))
        self.text2 = self.font2.render(str(self.fuel_level) + "%", True, (0, 255, 0, 255), (0, 0, 255, 255))
        self.text3 = self.font2.render(str(self.time), True, (0, 255, 0, 255), (0, 0, 255, 255))
        self.textRect = self.text.get_rect()
        self.textRect2 = self.text2.get_rect()
        self.textRect3 = self.text2.get_rect()
        self.textRect.center = (self.screen.get_width() // 2, 35)
        self.textRect2.center = (self.screen.get_width() // 2, 88)
        self.textRect3.center = ((self.screen.get_width() // 2) + 500, 88)

    def draw(self):
        self.screen.blit(self.text, self.textRect)
        self.screen.blit(self.text2, self.textRect2)
        self.screen.blit(self.text3, self.textRect3)
    def update_fuel_level(self):
        self.fuelCells_list.update_health()
        self.fuel_level = self.fuelCells_list.health
        self.fuel_level = round(self.fuel_level)
        self.text2 = self.font2.render(str(self.fuel_level) + "%", True, (0, 255, 0, 255), (0, 0, 255, 255))
        self.screen.blit(self.text2, self.textRect2)
        self.time = self.clock.get_time()
        self.text3 = self.font2.render(str(self.time), True, (0, 255, 0, 255), (0, 0, 255, 255))
        self.screen.blit(self.text3, self.textRect3)




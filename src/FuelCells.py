import pygame
import random
from FuelCell import FuelCell


class FuelCells:
    def __init__(self, screen, ship):
        self.screen = screen
        self.fuelCells_list = []
        self.ship = ship
        self.health = 100
        self.clock = pygame.time.Clock()
        for k in range(random.randint(5, 7)):
            self.fuelCells_list.append(FuelCell(screen, 5))

    def draw(self):
        for fuelCell in self.fuelCells_list:
            fuelCell.draw()

    def move(self):
        for fuelCell in self.fuelCells_list:
            fuelCell.move()

    def remove_charged_cells(self):
        for k in range(len(self.fuelCells_list) - 1, -1, -1):
            fuelCell = self.fuelCells_list[k]
            fuelCell.is_consumed(self.ship)
            if fuelCell.has_consumed or fuelCell.is_off_the_screen:
                del self.fuelCells_list[k]
                self.fuelCells_list.append(FuelCell(self.screen, 5))

    def update_health(self):
        for k in range(len(self.fuelCells_list) - 1, -1, -1):
            fuelCell = self.fuelCells_list[k]
            fuelCell.is_consumed(self.ship)
            if fuelCell.has_consumed:
                if self.health + 10 < 101:
                    self.health += 10
        self.clock.tick(1000)
        if round(self.clock.get_time()) % 2:
            self.health -= 0.15

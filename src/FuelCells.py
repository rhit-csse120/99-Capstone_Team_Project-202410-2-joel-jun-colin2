import pygame
import random

from pygame.time import set_timer

from FuelCell import FuelCell
from Starship import Ship


class FuelCells:
    def __init__(self, screen, ship):
        self.screen = screen
        self.fuelCells_list = []
        self.ship = ship
        for k in range(random.randint(5, 7)):
            self.fuelCells_list.append(FuelCell(screen, 3))

    def draw(self):

        # for fuelCell in self.fuelCells_list:
        #     events = pygame.event.get()
        #     events = fuelCell.draw()
        #     set_timer(events, 3, loops=1)
        # while True:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             break
        #     for fuelCell in self.fuelCells_list:
        #         fuelCell.draw()
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
                self.fuelCells_list.append(FuelCell(self.screen, 3))

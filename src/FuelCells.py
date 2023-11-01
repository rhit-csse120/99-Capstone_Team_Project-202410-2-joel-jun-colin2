import pygame
import random

from pygame.time import set_timer

from FuelCell import FuelCell
from Starship import Ship


class FuelCells:
    def __init__(self, screen, ship):
        self.screen = screen
        self.x_first = screen.get_width() // 2
        self.y_first = screen.get_height() // 2

        self.fuelCells_list = []
        self.ship = ship
        # if random.random() < 0.01:  # Adjust the probability as needed
        #     x_first = random.randint(0, screen.width)
        #     y_first = random.randint(0, screen.height)
        #     self.fuelCells_list.append(FuelCell(screen, x_first, y_first))
        for k in range(random.randint(9, 12)):
            self.fuelCells_list.append(FuelCell(screen, 3, self.x_first, self.y_first))
            self.x_first = random.randint(0, 1200)
            self.y_first = random.randint(0, 650)

    def draw(self):
        # while True:
        #     for fuelCell in self.fuelCells_list:
        #         fuelCell.draw()
        #     if
        #         break

        # for fuelCell in self.fuelCells_list:
        #     events = pygame.event.get()
        #     events = fuelCell.draw()
        #     set_timer(events, 3, loops=1)

        for fuelCell in self.fuelCells_list:
            fuelCell.draw()
    def move(self):
        for fuelCell in self.fuelCells_list:
            fuelCell.move()
    def remove_charged_cells(self):
        # for fuelCell in self.fuelCells_list:
        #     fuelCell.is_consumed(self.ship)
        #     if fuelCell.has_consumed:
        #         del fuelCell

        for k in range(len(self.fuelCells_list) - 1, -1, -1):
            fuelCell = self.fuelCells_list[k]
            fuelCell.is_consumed(self.ship)
            if fuelCell.has_consumed:
                del self.fuelCells_list[k]



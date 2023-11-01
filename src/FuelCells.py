import pygame
import random
from FuelCell import FuelCell


class FuelCells:
    def __init__(self, screen):
        self.screen = screen
        self.x_first = screen.get_width() // 2
        self.y_first = screen.get_height() // 2

        self.fuelCells_list = []
        # if random.random() < 0.01:  # Adjust the probability as needed
        #     x_first = random.randint(0, screen.width)
        #     y_first = random.randint(0, screen.height)
        #     self.fuelCells_list.append(FuelCell(screen, x_first, y_first))

        for k in range(random.randint(9, 12)):
            self.fuelCells_list.append(FuelCell(screen, 3, self.x_first, self.y_first ))
            self.x_first = random.randint(0, screen.width)
            self.y_first = random.randint(0, screen.height)

    def draw(self):
        for fuelCell in self.fuelCells_list:
            fuelCell.draw()

    def remove_passed_cells(self):  # Do I even need this?
        pass

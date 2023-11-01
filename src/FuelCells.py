import pygame
import random
from FuelCell import FuelCell

class FuelCells:
    def __init__(self, screen, x, y, ):
        self.screen = screen
        self.x = x
        self.y = y

        x_first = x
        y_first = y
        fuelCells_list = []
        if random.random() < 0.01:  # Adjust the probability as needed
            x_first = random.randint(0, screen.width)
            y_first = random.randint(0, screen.height)
            fuelCells_list.append(FuelCell(screen, x_first, y_first))

    def draw(self):
        for fuelCell in self.list_of_fuelCells:
            fuelCell.draw()

    def remove_passed_cells(self):          # Do I even need this?
        pass

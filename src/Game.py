"""
The  Game (model)  file for the Model-View-Controller architecture for our game.
1. It constructs all the objects specific to this game.
2. Its   draw_game   method is called repeatedly by the main game loop and
   typically asks each of the Game's objects to draw themselves.
3. Its   run_one_cycle   method is called repeatedly by the main game loop and
   typically asks each of the Game's objects to do whatever needs to happen
   independently of events / user-input.

Team members: Joel, Colin, Jun
"""
# DONE: Put the names of your entire team in the above doc-string.

import pygame
from Asteroid import Asteroid
from Asteroids import Asteroids
from Starship import Ship
from FuelCells import FuelCells
from FuelGauge import FuelGauge
import sys

# DONE: Put each class in its own module, using the same name for both.
#  Then use statements like the following, but for YOUR classes in YOUR modules:
#     from Fighter import Fighter


class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        # self.asteroid = Asteroid(screen)
        self.asteroids = Asteroids(screen)
        self.Ship = Ship(screen)
        self.fuelCells = FuelCells(screen, self.Ship)
        self.gauge = FuelGauge(screen, self.fuelCells)

        # DONE: Store whatever YOUR game needs, perhaps something like this:
        #     self.missiles = Missiles(self.screen)
        #     self.fighter = Fighter(self.screen, self.missiles)

    def draw_game(self):
        self.asteroids.draw()
        self.Ship.draw_self()
        self.fuelCells.draw()
        self.gauge.draw()

        """ Ask all the objects in the game to draw themselves. """
        # DONE: Use something like the following, but for objects in YOUR game:
        #     self.fighter.draw()

    def game_over(self):
        clock = pygame.time.Clock()
        game_over_image = pygame.image.load("../media/Game_Over_Screen-1.png")
        # size = (500,self.screen.get_height())
        # game_over_image = pygame.transform.scale(game_over_image, size)

        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.K_SPACE:
                    print("Restart!")
                    return
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((0,0,0))
            self.screen.blit(game_over_image, (250,250))
            pygame.display.update()

    def run_one_cycle(self):
        self.asteroids.move()
        self.asteroids.remove_asteroid()
        self.fuelCells.move()
        self.gauge.update_fuel_level()
        self.fuelCells.remove_charged_cells()


        """ All objects that do something at each cycle: ask them to do it. """
        # DONE: Use something like the following, but for objects in YOUR game:
        #     self.missiles.move()
        #     self.missiles.handle_explosions(self.enemies)

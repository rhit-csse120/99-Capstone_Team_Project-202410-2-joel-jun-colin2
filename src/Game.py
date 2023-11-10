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
from Enemy import Enemy

# DONE: Put each class in its own module, using the same name for both.
#  Then use statements like the following, but for YOUR classes in YOUR modules:
#     from Fighter import Fighter


class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.asteroids = Asteroids(screen)
        self.asteroid_field = self.asteroids.list_of_asteroids
        self.Ship = Ship(screen)
        self.fuelCells = FuelCells(screen, self.Ship)
        self.gauge = FuelGauge(screen, self.fuelCells)
        self.enemy = Enemy(screen, self.Ship)
        # DONE: Store whatever YOUR game needs, perhaps something like this:
        #     self.missiles = Missiles(self.screen)
        #     self.fighter = Fighter(self.screen, self.missiles)

    def draw_game(self):
        self.asteroids.draw()
        self.Ship.draw_self()
        self.fuelCells.draw()
        self.gauge.draw()
        self.enemy.draw()


        """ Ask all the objects in the game to draw themselves. """
        # DONE: Use something like the following, but for objects in YOUR game:
        #     self.fighter.draw()

    def game_over(self):
        clock = pygame.time.Clock()
        game_over_image = pygame.image.load("../media/Game_Over_Screen-1.png")
        size = (750, self.screen.get_height())
        game_over_image = pygame.transform.scale(game_over_image, size)

        while True:
            clock.tick(60)
            pressed_keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if pressed_keys[pygame.K_SPACE]:
                    print("Restart!")
                    self.Ship.has_exploded = False
                    return
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((0, 0, 0))
            self.screen.blit(game_over_image, (250, 0))
            pygame.display.update()

    def run_one_cycle(self):
        self.asteroids.move()
        self.asteroids.remove_asteroid()
        self.fuelCells.move()
        self.gauge.update_fuel_level()
        self.fuelCells.remove_charged_cells()
        self.Ship.is_hit_by(self.asteroid_field)

        """ All objects that do something at each cycle: ask them to do it. """
        # DONE: Use something like the following, but for objects in YOUR game:
        #     self.missiles.move()
        #     self.missiles.handle_explosions(self.enemies)
    def run_two_cycle(self):
        self.asteroids.move()
        self.asteroids.remove_asteroid()
        self.fuelCells.move()
        self.gauge.update_fuel_level()
        self.fuelCells.remove_charged_cells()
        self.Ship.is_hit_by(self.asteroid_field)
        self.enemy.move()

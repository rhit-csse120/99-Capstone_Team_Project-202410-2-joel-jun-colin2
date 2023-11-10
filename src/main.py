"""
The  main  file for the Model-View-Controller (MVC) architecture for our game.
It:
   1. Initializes pygame, the screen and a Clock (for the frame rate).
   2. Constructs a Game (model), View and Controller.
   3. Runs the game loop, which repeatedly (per the frame rate):
      -- Asks the Controller object to get and respond to events.
      -- Asks the Game object to run one cycle.
      -- Asks the View object to draw everything.

Team members: Joel, Jun, Colin
"""
# DONE: Put the names of your entire team in the above doc-string.

import pygame
from Game import Game
from Controller import Controller
from View import View
from Starship import Ship
import sys
import time
from Enemy import Enemy
from FuelGauge import FuelGauge
# from Asteroids import Asteroids

def start():
    pygame.init()
    pygame.display.set_caption("Jun's Space Odyssey")  # DONE: Put your own game name
    screen = pygame.display.set_mode((1200, 650))  # DONE: Choose your own size
    title_screen = pygame.image.load("../media/TitleScreen.png")
    title_screen = pygame.transform.scale(title_screen, (screen.get_width(), screen.get_height()))
    screen.blit(title_screen, (0, 0))
    pygame.display.update()
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if pressed_keys[pygame.K_RETURN]:
                main()
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()


def main():
    screen = pygame.display.set_mode((1200, 650))  # DONE: Choose your own size
    clock = pygame.time.Clock()
    game = Game(screen)  # the Model
    view = View(screen, game)  # the View
    controller = Controller(game)  # the Controller
    gauge = game.gauge
    start_time = time.time()
    # time_count = 0

    frame_rate = 60  # DONE: Choose your own frame rate

    while True:
        clock.tick(frame_rate)
        # time_count += 1/60
        controller.get_and_handle_events()
        game.run_one_cycle()
        view.draw_everything()
        if Ship.is_hit_by(game.Ship, game.asteroid_field) or gauge.fuel_level < 0:
            game.game_over()
            main()
        if time.time() > start_time + 60:
            level_2()
def level_2():
    pygame.init()
    pygame.display.set_caption("Jun's Space Odyssey")  # DONE: Put your own game name
    screen = pygame.display.set_mode((1200, 650))  # DONE: Choose your own size
    title_screen = pygame.image.load("../media/lvl2.png")
    title_screen = pygame.transform.scale(title_screen, (screen.get_width(), screen.get_height()))
    screen.blit(title_screen, (0, 0))
    pygame.display.update()
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if pressed_keys[pygame.K_SPACE]:
                main_2()
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
def main_2():
    screen = pygame.display.set_mode((1200, 650))  # DONE: Choose your own size
    clock = pygame.time.Clock()
    game = Game(screen)  # the Model
    view = View(screen, game)  # the View
    controller = Controller(game)  # the Controller
    gauge = game.gauge
    start_time = time.time()
    frame_rate = 60  # DONE: Choose your own frame rate
    while True:
        clock.tick(frame_rate)
        controller.get_and_handle_events()
        game.run_two_cycle()
        view.draw_everything()
        if Ship.is_hit_by(game.Ship, game.asteroid_field) or gauge.fuel_level < 0:
            game.game_over()
            main()
        if time.time() > start_time + 60:
            start()
start()

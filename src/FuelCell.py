import pygame


class FuelCell:
    def __init__(self, screen, speed, x=100, y=100):
        self.screen = screen
        self.image = pygame.image.load()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = x
        self.y = y
        self.speed = speed
        self.is_off_the_screen = False
        self.is_consumed = False
        self.has_charged = False
        self.charge_sound = pygame.mixer.Sound()  # Find a sound

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    # def is_consumed(self, ship: Ship):
    #     fuel_rect = pygame.Rect(self.x, self.y, self.width, self.height)
    #     ship_rect = pygame.Rect(ship.x, ship.y, ship.width, ship.height)
    #     return fuel_rect.colliderect(ship_rect)
    def move(self):
        self.x -= self.speed
        if self.y > self.screen.get_height():
            self.is_off_the_screen = True

    def charge(self):
        self.charge_sound.play()
        self.has_charged = True

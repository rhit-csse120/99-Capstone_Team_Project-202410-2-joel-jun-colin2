import pygame


class FuelGauge:
    # def __init__(self, screen):
    #     self.screen = screen
    #     self.font = pygame.font.Font('Gauge', 100)
    #     self.text = self.font.render('Gauge', True, (0, 255, 0, 255), (0, 0, 255, 255))
    #     self.textRect = self.text.get_rect()
    #     self.textRect.center = (self.screen.get_width() // 2, 10)

    def draw(self):
        self.screen.blit(self.text, self.textRect)

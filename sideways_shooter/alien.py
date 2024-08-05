import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, sws_game):
        """initializes the necessary attributes"""
        super().__init__()
        self.screen = sws_game.screen
        self.screen_rect = sws_game.screen_rect
        self.settings = sws_game.settings

        # load image, transform image to tilt left, position it to mid-right
        self.image = pygame.image.load("../images/alien.png")
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.midright = self.screen_rect.topright

        # float y value of rect
        self.y = float(self.rect.y)

    def update(self):
        """update the position of the alien"""
        self.y += self.settings.alien_speed * self.settings.fleet_direction

        self.rect.y = self.y

    def check_edges(self):
        """check if the fleet hit the edges"""
        screen_rect = self.screen.get_rect()
        # return true if it hit bottom edge
        return (self.rect.top <= 0) or (self.rect.bottom >= self.screen_rect.bottom)

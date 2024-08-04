import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, sws_game):
        """initializes the necessary attributes"""
        super().__init__()
        self.screen_rect = sws_game.screen_rect

        self.image = pygame.image.load("../images/alien.png")
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.midright = self.screen_rect.midright

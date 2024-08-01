import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    def __init__(self, rain_main):
        super().__init__()
        self.image = pygame.image.load("../images/rain_drop.png")
        self.rect = self.image.get_rect()


class Rain:
    pass

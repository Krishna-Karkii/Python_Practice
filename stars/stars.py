import pygame
from pygame.sprite import Sprite


class Stars(Sprite):
    """This class is about pygame window with random stars"""
    def __init__(self):
        """initialize attributes of the stars"""
        super().__init__()
        # Load pygame resources
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.image = pygame.image.load("../images/star.png")


import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    """Class to create the instance of rain drop"""
    def __init__(self, rain_main):
        super().__init__()
        self.image = pygame.image.load("../images/rain_drop.png")
        self.rect = self.image.get_rect()


class Rain:
    """Class to create the rain animation"""
    def __init__(self):
        # Load the resources
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()

    def run_animation(self):
        """Main loop of the animation"""
        pass

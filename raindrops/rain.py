import sys

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

        self.clock = pygame.time.Clock()

    def run_animation(self):
        """Main loop of the animation"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    rain = Rain()
    rain.run_animation()
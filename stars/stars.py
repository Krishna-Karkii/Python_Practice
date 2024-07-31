import sys
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

    def run_stars(self):
        """main loop of this function"""
        while True:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    sys.exit()

                elif self.event.type == pygame.KEYDOWN:
                    if self.event.key == pygame.K_q:
                        sys.exit()

            pygame.display.flip()


if __name__ == "__main__":
    star = Stars()
    star.run_stars()
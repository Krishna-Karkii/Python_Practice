import sys
import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """this is the instance of the star"""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("../images/star.png")
        self.image_rect = self.image.get_rect()


class Stars:
    """This class is about pygame window with random stars"""
    def __init__(self):
        """initialize attributes of the stars"""
        # Load pygame resources
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.star = Star()
        self.star.image_rect.center = self.screen_rect.center

        self.stars = pygame.sprite.Group()
        self.clock = pygame.time.Clock()

    def run_stars(self):
        """main loop of this function"""
        while True:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    sys.exit()

                elif self.event.type == pygame.KEYDOWN:
                    if self.event.key == pygame.K_q:
                        sys.exit()

            self._blitme()
            pygame.display.flip()
            self.clock.tick(60)

    def create_star(self):
        pass

    def _blitme(self):
        self.screen.blit(self.star.image, self.star.image_rect, self.screen_rect)


if __name__ == "__main__":
    star = Stars()
    star.run_stars()

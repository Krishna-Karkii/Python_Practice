import sys
import random
import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """this is the instance of the star"""
    def __init__(self, stars):
        """initialize the attributes of the star"""
        super().__init__()
        self.image = pygame.image.load("../images/star.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, stars.screen_rect.width)
        self.rect.y = random.randint(0, stars.screen_rect.height)


class Stars:
    """This class is about pygame window with random stars"""
    def __init__(self):
        """initialize attributes of the stars"""
        # Load pygame resources
        pygame.init()
        # create window in full screen mode
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()

        # create stars group to catch a list of star instance
        self.stars = pygame.sprite.Group()

        # create clock to maintain frame rate
        self.clock = pygame.time.Clock()

    def run_stars(self):
        """main loop of this function"""
        while True:
            # check for event related to quiting
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    sys.exit()

                elif self.event.type == pygame.KEYDOWN:
                    if self.event.key == pygame.K_q:
                        sys.exit()

            self._update_star()
            pygame.display.flip()
            self.clock.tick(60)

    def _create_star(self):
        """instance of the star is created, and added in the stars group"""
        if len(self.stars.sprites()) == 0:
            while len(self.stars.sprites()) < 10:
                new_star = Star(self)
                self.stars.add(new_star)

    def _update_star(self):
        """draw the star in the screen"""
        self._create_star()
        self.stars.draw(self.screen)


if __name__ == "__main__":
    star = Stars()
    star.run_stars()

import pygame


class Ship:
    """This class handles things related to ship."""
    def __init__(self, tp_game):
        """initialize the necessary attributes required to manage the ship."""
        self.screen = tp_game.screen
        self.screen_rect = tp_game.screen_rect

        # load the image and rotate it
        self.image = pygame.image.load("../images/spaceship_tp.png")
        self.image = pygame.transform.rotate(self.image, 90)

        # position the ship initially on mid-left of the window
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

    def blit_me(self):
        """blit the ship image to the surface."""
        self.screen.blit(self.image, self.rect)
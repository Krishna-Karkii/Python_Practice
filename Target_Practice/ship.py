import pygame


class Ship:
    """This class handles things related to ship."""
    def __init__(self, tp_game):
        """initialize the necessary attributes required to manage the ship."""
        self.screen = tp_game.screen
        self.screen_rect = tp_game.screen_rect
        self.settings = tp_game.settings

        # load the image and rotate it
        self.image = pygame.image.load("../images/spaceship_tp.png")
        self.image = pygame.transform.rotate(self.image, 90)

        # position the ship initially on mid-left of the window
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        # movement flag for ship position
        self.up_flag = False
        self.down_flag = False

        # store initial position of the ship
        self.y = float(self.rect.y)

    def blit_me(self):
        """blit the ship image to the surface."""
        self.screen.blit(self.image, self.rect)

    def update_ship_pos(self):
        """update the position of the ship on key press"""
        if self.down_flag:
            self.y += self.settings.ship_speed
        if self.up_flag:
            self.y -= self.settings.ship_speed

        self.rect.y = self.y


import pygame


class Ship:
    """A class related to ship updates"""
    def __init__(self, sws_game):
        """initializes the settings of ship"""
        pygame.init()
        self.screen = sws_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = sws_game.settings

        # Loading the image, rotating 90 degrees, and setting its position
        self.image = pygame.image.load("../images/sideway_ship.png")
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)

        # movement flag
        self.up_flag = False
        self.down_flag = False

    def blitme(self):
        """displays ship image on the surface"""
        self.screen.blit(self.image, self.rect)

    def update_ship_position(self):
        """updates ship position"""
        if self.up_flag and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        if self.down_flag and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y

    def center_ship(self):
        """center the ships position respective to screen rect"""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

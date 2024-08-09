from pygame.sprite import Sprite
import pygame


class Bullet(Sprite):
    """Contains methods and attributes related to bullets."""

    def __init__(self, tp_game):
        """initialize the necessary attributes of the bullet class"""
        super().__init__()
        self.screen = tp_game.screen
        self.screen_rect = tp_game.screen_rect
        self.settings = tp_game.settings
        self.ship = tp_game.ship

        # create a bullet rect and position it
        self.rect = pygame.Rect(0, 0, self.settings.bullet_height, self.settings.bullet_width)
        self.rect.midleft = self.ship.rect.midright

        # exact position of the bullet
        self.x = float(self.rect.x)

    def update(self):
        """update the position of the bullets."""
        self.x += self.settings.bullet_speed

        self.rect.x = self.x

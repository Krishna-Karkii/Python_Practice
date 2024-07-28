import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class that handles activities related to bullet"""
    def __init__(self, sws_game):
        """initializes bullet attributes"""
        super().__init__()

        self.game = sws_game
        self.screen = sws_game.screen
        self.screen_rect = self.screen.get_rect()
        self.color = sws_game.settings.bullet_color

        self.rect = pygame.Rect(0, 0, sws_game.settings.bullet_width, sws_game.settings.bullet_height)
        self.rect.midtop = self.game.ship.image_rect.midright

        self.x = float(self.rect.x)

    def update(self):
        """update the bullet position"""
        self.x += self.game.settings.bullet_speed

        self.rect.x = self.x

    def draw(self):
        """draw the bullet on the surface"""
        pygame.draw.rect(self.screen, self.color, self.rect)


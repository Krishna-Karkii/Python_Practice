import pygame.font


class PKeyInfo:
    """This is a class related to text information for user to understand
    specifics of the game"""
    def __init__(self, sws_game):
        self.screen = sws_game.screen
        self.screen_rect = sws_game.screen_rect

        # define the properties and dimension of text
        self.width, self.height = 1000, 40
        self.font_color = (80, 80, 80)
        self.bg_color = (128, 128, 128)
        self.font = pygame.font.SysFont(None, 38)

        # create text rect and position it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midtop = self.screen_rect.midtop

        self._prep_msg()

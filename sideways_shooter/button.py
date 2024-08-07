import pygame.font


class Button:
    """This class creates a button on the screen"""
    def __init__(self, sws_game, msg):
        """initialize attributes of button class"""
        self.screen = sws_game.screen
        self.screen_rect = self.screen.get_rect()

        # define button dimensions and text properties
        self.width, self.height = 200, 50
        self.text_color = (255, 255, 255)
        self.button_color = (0, 0, 135)
        self.font = pygame.font.SysFont(None, 48)

        # create rect and define its position
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)


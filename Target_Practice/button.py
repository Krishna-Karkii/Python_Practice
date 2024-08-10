import pygame.font


class Button:
    """This class contains methods and attributes related to buttons."""

    def __init__(self, tp_game):
        self.screen = tp_game.screen
        self.screen_rect = tp_game.screen_rect

        # button settings and dimensions, font properties
        self.button_width = 200
        self.button_height = 50
        self.button_color = (0, 135, 0)
        self.font_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # create button rect and position it
        self.rect = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.rect.center = self.screen_rect.center

        self._prep_msg("Play")

    def _prep_msg(self, msg):
        """creates a message image, centers it"""
        self.msg_image = self.font.render(msg, True, self.font_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def display_button(self):
        """display the button on the surface."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

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
        self._define_position(msg)

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """render an image of text and center it to the rect"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """draw the button on the screen"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def _define_position(self, msg):
        """Define the position of the rect based on the msg"""
        # default position for Play and Medium button
        self.rect.center = self.screen_rect.center

        # check the msg and define the position of the rect
        if msg == "Easy":
            self.rect.centery -=100

        elif msg == "Hard":
            self.rect.centery += 100


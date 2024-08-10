import pygame


class Box:
    """contains everything related to the box."""

    def __init__(self, tp_game):
        """initialize the attributes of the box."""
        self.screen = tp_game.screen
        self.screen_rect = tp_game.screen_rect
        self.settings = tp_game.settings

        # create a box rect and set its position
        self.rect = pygame.Rect(0, 0, self.settings.box_width, self.settings.box_height)
        self.rect.bottomright = self.screen_rect.bottomright

        # store the float value y of box position
        self.y = float(self.rect.y)

    def draw_box(self):
        """blit the box rect on the surface."""
        pygame.draw.rect(self.screen, self.settings.box_color, self.rect)

    def check_edges(self):
        """check if box has hit the top edge or bottom edge."""
        return (self.rect.bottom >= self.settings.screen_height) or (self.rect.top <= 0)

    def update(self):
        """update the box position not crossing the edges."""
        self.y += self.settings.box_speed * self.settings.box_direction

        self.rect.y = self.y

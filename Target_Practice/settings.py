class Settings:
    """This class contains the main settings of the game."""

    def __init__(self):
        """initialize the default settings of the game."""
        self.screen_width = 1200
        self.screen_height = 800

        # main window background color
        self.screen_bg_color = (130, 130, 130)

        # ship settings
        self.ship_speed = 1.5

        # bullet settings
        self.bullet_speed = 3.0
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (40, 35, 35)

        # box settings
        self.box_height = 55
        self.box_width = 50
        self.box_color = (230, 230, 230)
        self.box_speed = 1

        # -1 for up, 1 for down
        self.box_direction = 1

    def initialize_box_settings(self):
        """initialize the box settings of the game."""
        self.box_direction = 1
        self.box_speed = 1

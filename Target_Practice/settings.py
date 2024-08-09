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

class Settings:
    """A class that handles activities related to settings"""
    def __init__(self):
        """initialize the default settings"""
        # settings related to bullet
        self.bullet_width = 20
        self.bullet_height = 5
        self.bullet_color = (255, 128, 128)

        # alien settings
        self.drop_left = 15

        # Default game statistics
        self.ships_allowed = 3

        # scale at which game speeds up
        self.speedup_scale = 1.2

    def initialize_dynamic_settings(self):
        """Dynamic settings of the game are initialized."""
        self.alien_speed = 2.0
        self.bullet_speed = 5.0
        self.ship_speed = 3.0

        # -1 for moving up and 1 for moving down
        self.fleet_direction = 1

    def speed_up(self):
        """Speed up the game if fleet destroyed."""
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale

    def initialize_medium_settings(self):
        """initialize the medium settings for the game."""
        self.alien_speed = 3.0
        self.bullet_speed = 6.0
        self.ship_speed = 4.0

        # -1 for moving up and 1 for moving down
        self.fleet_direction = 1

    def initialize_hard_settings(self):
        """initialize the hard settings for the game."""
        self.alien_speed = 4.0
        self.bullet_speed = 8.0
        self.ship_speed = 5.0

        # -1 for moving up and 1 for moving down
        self.fleet_direction = 1


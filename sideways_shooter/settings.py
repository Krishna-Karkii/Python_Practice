class Settings:
    """A class that handles activities related to settings"""
    def __init__(self):
        # Settings related to movement
        self.ship_speed = 2.5

        # settings related to bullet
        self.bullet_speed = 3.0
        self.bullet_width = 20
        self.bullet_height = 5
        self.bullet_color = (255, 128, 128)

        # alien settings
        self.alien_speed = 1.5
        # -1 for moving up and 1 for moving down
        self.fleet_direction = 1
        self.drop_left = 100

        # Default game statistics
        self.ships_allowed = 3

class Settings:
    """A class that handles activities related to settings"""
    def __init__(self):
        # Settings related to movement
        self.ship_speed = 1.5

        # settings related to bullet
        self.bullet_speed = 2.0
        self.bullet_width = 20
        self.bullet_height = 5
        self.bullet_color = (255, 128, 128)
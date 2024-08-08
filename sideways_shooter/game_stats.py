class GameStats:
    """This class covers everything related to game statistics.
    ex: game score, number of ships left"""
    def __init__(self, sws_game):
        """Initialize the default statistics"""
        super().__init__()
        self.settings = sws_game.settings

        self.reset_settings()

    def reset_settings(self):
        self.ship_count = self.settings.ships_allowed

class GameStats:
    """This class covers everything related to game statistics.
    ex: game score, number of ships left"""
    def __init__(self, sws_game):
        """Initialize the default statistics"""
        super().__init__()
        self.settings = sws_game.settings
        self.high_score = self._get_high_score()

        self.reset_settings()

    def reset_settings(self):
        """reset the stats when the function is called."""
        self.ship_count = self.settings.ships_allowed
        self.score = 0
        self.level = 1

    def check_high_score(self):
        """This method checks and updates the high score,
        if the current score is greater."""
        if self.score > self.high_score:
            self.high_score = self.score
            # write the new high score to the file
            with open("hs.txt", 'w') as file:
                file.write(str(self.high_score))

    def _get_high_score(self):
        """Get the high score from the stored file."""
        with open("hs.txt", 'r') as file:
            hs = file.read()

        return int(hs)

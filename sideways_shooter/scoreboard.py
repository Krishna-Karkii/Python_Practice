import pygame


class ScoreBoard:
    """Creates and displays object on the screen related to scoring."""
    def __init__(self, sws_game):
        """initialize the defaults of the scoreboard."""
        self.screen = sws_game.screen
        self.screen_rect = sws_game.screen_rect
        self.stats = sws_game.game_stats

        # set the font color and size for the scoring
        self.font_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 40)

        self.prep_score()

    def prep_score(self):
        """This method creates current user score."""
        score = str(self.stats.score)
        self.score_img = self.font.render(score, True, self.font_color)
        self.score_img_rect = self.score_img.get_rect()
        self.score_img_rect.right = self.screen_rect.right - 20
        self.score_img_rect.top = 20

    def draw(self):
        """This method draws the prepared images related to scoring."""
        self.screen.blit(self.score_img, self.score_img_rect)

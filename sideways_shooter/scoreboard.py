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
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """This method creates current user score image."""
        # round the score to the nearest 10s
        score = f"{round(self.stats.score, -1):,}"
        self.score_img = self.font.render(score, True, self.font_color)
        self.score_img_rect = self.score_img.get_rect()
        self.score_img_rect.right = self.screen_rect.right - 20
        self.score_img_rect.top = 20

    def prep_high_score(self):
        """This method creates the user high score image,
        and set its position."""
        # round the high score to nearest 10s
        high_score = f"High_score: {round(self.stats.high_score, -1):,}"
        self.hs_img = self.font.render(high_score, True, self.font_color)
        self.hs_img_rect = self.hs_img.get_rect()
        self.hs_img_rect.center = self.screen_rect.center
        self.hs_img_rect.top = 20

    def prep_level(self):
        """creates the level image, set its position"""
        level = str(self.stats.level)
        self.lvl_img = self.font.render(level, True, self.font_color)
        self.lvl_img_rect = self.lvl_img.get_rect()
        self.lvl_img_rect.right = self.score_img_rect.right
        self.lvl_img_rect.top = self.score_img_rect.top + 50


    def draw(self):
        """This method draws the prepared images related to scoring."""
        self.screen.blit(self.score_img, self.score_img_rect)
        self.screen.blit(self.hs_img, self.hs_img_rect)
        self.screen.blit(self.lvl_img, self.lvl_img_rect)

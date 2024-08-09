import sys
import pygame

from settings import Settings


class TargetPractice:
    """This class handles everything related to target practice game.
    This is the main class which runs the game."""

    def __init__(self):
        """initialize the necessary attributes of TargetPractice class."""
        pygame.init()

        self.settings = Settings()

        # Create main screen for game to display
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Target Practice")

        # To control the frames of the game
        self.clock = pygame.time.Clock()

    def run_game(self):
        """This method contains the main loop of the game."""
        # main loop of the game
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.screen_bg_color)
            pygame.display.flip()

            # control the pace of the loop for 60 fps
            self.clock.tick(60)


if __name__ == "__main__":
    tp = TargetPractice()
    tp.run_game()
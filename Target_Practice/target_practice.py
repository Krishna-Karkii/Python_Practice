import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


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

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """This method contains the main loop of the game."""
        # main loop of the game
        while True:
            self._check_events()

            self._update_window()
            pygame.display.flip()

            # control the pace of the loop for 60 fps
            self.clock.tick(60)

    def _check_events(self):
        """Responds to the mouse and keyboard inputs."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup(event)

    def _check_keydown(self, event):
        """check event related to the keydown"""
        if event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_UP:
            self.ship.up_flag = True

        elif event.key == pygame.K_DOWN:
            self.ship.down_flag = True

        elif event.key == pygame.K_SPACE:
            self._create_bullet()

    def _check_keyup(self, event):
        """check event related to the key up."""
        if event.key == pygame.K_UP:
            self.ship.up_flag = False

        elif event.key == pygame.K_DOWN:
            self.ship.down_flag = False

    def _update_window(self):
        """update the window before flipping it."""
        self.screen.fill(self.settings.screen_bg_color)
        self.ship.blit_me()

        # draw every bullet on bullets group on surface
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # update the ship and bullet position
        self.ship.update_ship_pos()
        self.bullets.update()

    def _create_bullet(self):
        """create a bullet instance and add it in bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


if __name__ == "__main__":
    tp = TargetPractice()
    tp.run_game()

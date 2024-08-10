import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from box import Box
from button import Button


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

        # create the instance of ship and box
        self.ship = Ship(self)
        self.box = Box(self)

        self.bullets = pygame.sprite.Group()

        self.button = Button(self)

        # count the no of bullets, game active flag
        self.count = 0
        self.game_active = False

    def run_game(self):
        """This method contains the main loop of the game."""
        # main loop of the game
        while True:
            self._check_events()

            self._bullet_box_collision()
            self._update_window()
            self._end_game()
            if not self.game_active:
                self.button.display_button()
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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

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

        # blit the objects on the surface
        self.ship.blit_me()
        self.box.draw_box()

        # draw every bullet on bullets group on surface
        if self.game_active:
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()

            # update the ship, box, and bullet position
            self.ship.update_ship_pos()
            self._update_box()
            self.bullets.update()

        self._remove_bullet()

    def _create_bullet(self):
        """create a bullet instance and add it in bullets group."""
        # only create bullet upto 3 bullets
        if len(self.bullets.sprites()) < 3:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _remove_bullet(self):
        """remove bullet from the group is disappeared from the edge"""
        for bullet in self.bullets.sprites().copy():
            if bullet.disappeared():
                self.bullets.remove(bullet)
                self.count += 1

    def _update_box(self):
        """check edges, and update the position of the box."""
        if self.box.check_edges():
            self.settings.box_direction *= -1
        self.box.update()

    def _bullet_box_collision(self):
        """check if the bullet collided with the box."""
        pygame.sprite.spritecollide(self.box, self.bullets, True)

    def _end_game(self):
        """end the game when the player missed 3 times"""
        if self.count >= 3:
            self.game_active = False

    def _check_play_button(self, mouse_pos):
        """check if the mouse point and play button collided"""
        if self.button.rect.collidepoint(mouse_pos) and not self.game_active:
            self.game_active = True


if __name__ == "__main__":
    tp = TargetPractice()
    tp.run_game()

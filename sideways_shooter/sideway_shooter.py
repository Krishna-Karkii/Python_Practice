import sys
import pygame
import time

from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from text_info import PKeyInfo


class SideWayShooter:
    """A main class that controls the game"""
    def __init__(self):
        """set the default attributes of the game"""
        pygame.init()

        # initialize the window of the game
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Sideway Shooters")
        self.screen_rect = self.screen.get_rect()

        self.clock = pygame.time.Clock()

        self.settings = Settings()

        # instance of game stats to store game points, ship lefts etc.
        self.game_stats = GameStats(self)

        # create instance of imported, create bullets group for bullet instance
        # create alien group for alien instance
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.game_active = False
        self.button = Button(self, "Play")
        self.p_key_info = PKeyInfo(self)

    def run_game(self):
        """This function contains the main loop of the game"""
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update_ship_position()
                self._update_bullet()
                self._update_aliens()
            self._update_display()
            if not self.game_active:
                self.button.draw()
                self.p_key_info.render_text()
            pygame.display.flip()
            self.clock.tick(60)

    def _check_keydown(self):
        """check which key is pressed, set flag to true"""
        if self.event.key == pygame.K_UP:
            self.ship.up_flag = True
        if self.event.key == pygame.K_DOWN:
            self.ship.down_flag = True
        if self.event.key == pygame.K_SPACE:
            self._fire_bullet()
        if self.event.key == pygame.K_q:
            sys.exit()
        if self.event.key == pygame.K_p:
            self._check_play_button(mouse_pos="", key_pressed=True)

    def _check_keyup(self):
        """check which key was released, set flag to false"""
        if self.event.key == pygame.K_UP:
            self.ship.up_flag = False

        if self.event.key == pygame.K_DOWN:
            self.ship.down_flag = False

    def _check_play_button(self, mouse_pos, key_pressed):
        """manages the action when play button is pressed"""
        collide = False
        if mouse_pos != "":
            collide = self.button.rect.collidepoint(mouse_pos)

        # only work if the "P" key pressed or button pressed
        if (collide and not self.game_active) or (key_pressed and not self.game_active):
            # reset the game stats
            self.game_stats.reset_settings()
            self.game_active = True

            # empty the bullets and aliens group
            self.bullets.empty()
            self.aliens.empty()

            # create a new fleet, and recenter the ship
            self._create_fleet()
            self.ship.center_ship()

            # hide cursor
            pygame.mouse.set_visible(False)

    def _check_events(self):
        """check events from the recent events"""
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                sys.exit()
            elif self.event.type == pygame.KEYDOWN:
                self._check_keydown()
            elif self.event.type == pygame.KEYUP:
                self._check_keyup()
            elif self.event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos, key_pressed=False)

    def _fire_bullet(self):
        """create a new bullet instance every time space bar is clicked"""
        # create and add no more than 5 bullets
        if len(self.bullets.sprites()) < 5:
            self.bullet = Bullet(self)
            self.bullets.add(self.bullet)

    def _create_alien(self, position_y, position_x):
        """create alien instance and add it to aliens groups"""
        alien = Alien(self)
        alien.y = position_y
        alien.rect.x = position_x
        alien.rect.y = position_y
        self.aliens.add(alien)

    def _create_fleet(self):
        """This creates a fleet of alien"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_y = alien_height
        current_x = alien.rect.x

        # add aliens horizontally and vertically leaving enough space between ship and aliens
        while current_x > 10 * alien_width:
            while current_y < (self.screen_rect.height - 2 * alien_height):
                self._create_alien(current_y, current_x)
                current_y += 2 * alien_height

            current_y = alien_height
            current_x -= 2 * alien_width

    def _update_display(self):
        """update the display before flipping it"""
        self.screen.fill((128, 128, 128))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw()
        self.aliens.draw(self.screen)

    def _update_bullet(self):
        """update the bullet position and remove unnecessary bullets"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen_rect.right:
                self.bullets.remove(bullet)

    def _ship_hit(self):
        """This method handles the game stats,
         empties the bullets and aliens,
         and ship position when the ship is hit"""
        if self.game_stats.ship_count > 0:
            self.game_stats.ship_count -= 1

            # empty the bullets and remaining alien fleet
            self.bullets.empty()
            self.aliens.empty()

            # create a new fleet and center the ship position
            self._create_fleet()
            self.ship.center_ship()

            time.sleep(0.5)

        else:
            # set game active to false, initialize dynamics after game over.
            self.game_active = False
            self.settings.initialize_dynamic_settings()
            pygame.mouse.set_visible(True)

    def _change_fleet_direction(self):
        """change the direction, and dropdown the fleet"""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.drop_left
        self.settings.fleet_direction *= -1

    def _check_fleet_edges(self):
        """check whether an alien has hit the edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _check_alien_status(self):
        """respond to alien-bullet collisions, and create new fleet"""
        # respond to collision between bullet and ship
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # create if all alien destroyed
        if not self.aliens:
            # speed up the game.
            self.settings.speed_up()
            self.bullets.empty()
            self._create_fleet()

    def _check_bottom_hit(self):
        """check if the alien has hit the bottom"""
        for alien in self.aliens.sprites():
            if alien.rect.left <= 0:
                self._ship_hit()
                break

    def _update_aliens(self):
        """update the position of the aliens."""
        self._check_alien_status()
        self._check_fleet_edges()
        self.aliens.update()

        # execute when the ship and alien collides
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # check if the alien has hit the bottom screen
        self._check_bottom_hit()


if __name__ == "__main__":
    sws = SideWayShooter()
    sws.run_game()

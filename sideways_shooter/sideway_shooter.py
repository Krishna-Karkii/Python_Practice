import sys
import pygame
import time

from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien
from game_stats import GameStats


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

    def run_game(self):
        """This function contains the main loop of the game"""
        while True:
            self._check_events()
            self._update_bullet()
            self._update_aliens()
            self._update_display()
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

    def _check_keyup(self):
        """check which key was released, set flag to false"""
        if self.event.key == pygame.K_UP:
            self.ship.up_flag = False

        if self.event.key == pygame.K_DOWN:
            self.ship.down_flag = False

    def _check_events(self):
        """check events from the recent events"""
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                sys.exit()
            elif self.event.type == pygame.KEYDOWN:
                self._check_keydown()
            elif self.event.type == pygame.KEYUP:
                self._check_keyup()

    def _fire_bullet(self):
        """create a new bullet instance every time space bar is clicked"""
        # create and add no more than 6 bullets
        if len(self.bullets.sprites()) < 6:
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
        self.ship.update_ship_position()
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
        self.game_stats.ship_count -= 1

        # empty the bullets and remaining alien fleet
        self.bullets.empty()
        self.aliens.empty()

        # create a new fleet and center the ship position
        self._create_fleet()
        self.ship.center_ship()

        time.sleep(0.5)

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
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """update the position of the aliens"""
        self._check_alien_status()
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()


if __name__ == "__main__":
    sws = SideWayShooter()
    sws.run_game()

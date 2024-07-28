import sys
import pygame
from ship import Ship
from settings import Settings
from bullet import Bullet


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

        # create instance of imported, create bullets group for bullet instance
        self.settings = Settings()
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """This function contains the main loop of the game"""
        while True:
            self._check_events()
            self._update_bullet()
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
        self.bullet = Bullet(self)
        self.bullets.add(self.bullet)

    def _update_display(self):
        """update the display before flipping it"""
        self.screen.fill((128, 128, 128))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw()
        self.ship.update_ship_position()

    def _update_bullet(self):
        """update the bullet position and remove unnecessary bullets"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen_rect.right:
                self.bullets.remove(bullet)


if __name__ == "__main__":
    sws = SideWayShooter()
    sws.run_game()

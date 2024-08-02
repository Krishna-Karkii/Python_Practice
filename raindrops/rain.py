import sys
import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    """Class to create the instance of rain drop"""
    def __init__(self, rain_main):
        super().__init__()
        self.screen = rain_main.screen
        self.image = pygame.image.load("../images/rain_drop.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def update(self):
        self.y += 1.5
        self.rect.y = self.y

    def check_disappeared(self):
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False


class Rain:
    """Class to create the rain animation"""
    def __init__(self):
        # Load the resources
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()

        self.clock = pygame.time.Clock()
        self.raindrops = pygame.sprite.Group()

        self._create_rain_fleet()

    def run_animation(self):
        """Main loop of the animation"""
        while True:
            self._check_events()
            self._update_rain_fleet()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """check event form the event list"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _create_raindrop(self, position_x, position_y):
        """create the instance of the rain drop"""
        new_drop = Raindrop(self)
        new_drop.y = position_y
        new_drop.rect.x = position_x
        new_drop.rect.y = position_y
        self.raindrops.add(new_drop)

    def _create_rain_fleet(self):
        """create a fleet of rain horizontally"""
        drop = Raindrop(self)
        drop_width, drop_height = drop.rect.size
        current_x = drop_width
        current_y = drop_height

        # create four rows of droplets
        while current_y < (self.screen_rect.height - 6 * drop_height):

            while current_x < (self.screen_rect.width - 2 * drop_width):
                self._create_raindrop(current_x, current_y)
                current_x += 2 * drop_width

            current_y += 2 * drop_height
            current_x = drop_width

    def _create_row(self):
        drop = Raindrop(self)
        drop_width, drop_height = drop.rect.size
        current_y = -1 * drop_height
        current_x = drop_width

        while current_x < (self.screen_rect.width - 2 * drop_width):
            self._create_raindrop(current_x, current_y)
            current_x += 2 * drop_width

    def _update_rain_fleet(self):
        """update and draw the position of rain drops on surface"""
        self.raindrops.update()

        # Assume we won't make new drops.
        make_new_drops = False
        for drop in self.raindrops.copy():
            if drop.check_disappeared():
                # Remove this drop, and we'll need to make new drops.
                self.raindrops.remove(drop)
                make_new_drops = True

        # Make a new row of drops if needed.
        if make_new_drops:
            self._create_row()

    def _update_screen(self):
        """"""
        self.screen.fill((230, 230, 230))
        self.raindrops.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    rain = Rain()
    rain.run_animation()

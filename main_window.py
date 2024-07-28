import pygame
import sys
from character import Character


class Main:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.rect_screen = self.screen.get_rect()
        pygame.display.set_caption("Experiment")

        self.clock = pygame.time.Clock()

        self.character = Character(self)

    def run_main(self):
        while True:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    sys.exit()
                elif self.event.type == pygame.KEYDOWN:
                    self._check_keydown()
                elif self.event.type == pygame.KEYUP:
                    self._check_keyup()

            self.character.update_ship()
            self._update_window()

            self.clock.tick(60)

    def _update_window(self):
        self.screen.fill((135, 206, 235))
        self.character.blitme()
        pygame.display.flip()

    def _check_keydown(self):
        if self.event.key == pygame.K_DOWN:
            self.character.down_flag = True
        if self.event.key == pygame.K_UP:
            self.character.up_flag = True
        if self.event.key == pygame.K_RIGHT:
            self.character.right_flag = True
        if self.event.key == pygame.K_LEFT:
            self.character.left_flag = True
        if self.event.key == pygame.K_q:
            sys.exit()

    def _check_keyup(self):
        if self.event.key == pygame.K_DOWN:
            self.character.down_flag = False
        if self.event.key == pygame.K_UP:
            self.character.up_flag = False
        if self.event.key == pygame.K_RIGHT:
            self.character.right_flag = False
        if self.event.key == pygame.K_LEFT:
            self.character.left_flag = False


if __name__ == "__main__":
    mn = Main()
    mn.run_main()


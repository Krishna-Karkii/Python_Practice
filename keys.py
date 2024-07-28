import sys
import pygame


class Keys:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Exercise")

        self.clock = pygame.time.Clock()

        self.right_flag = False
        self.left_flag = False
        self.up_flag = False
        self.down_flag = False

    def check_keys(self):
        while True:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    sys.exit()

                if self.event.type == pygame.KEYDOWN:
                    if self.event.key == pygame.K_RIGHT:
                        self.right_flag = True
                    if self.event.key == pygame.K_LEFT:
                        self.left_flag = True
                    if self.event.key == pygame.K_UP:
                        self.up_flag = True
                    if self.event.key == pygame.K_DOWN:
                        self.down_flag = True

                elif self.event.type == pygame.KEYUP:
                    self._check_keyup()

                self._check_keydown()
                self._update_window()
                self.clock.tick(60)

    def _update_window(self):
        self.screen.fill((20, 30, 30))
        pygame.display.flip()

    def _check_keydown(self):
        if self.left_flag:
            print("Left arrow key.")

        if self.right_flag:
            print("Right arrow key.")

        if self.up_flag:
            print("Up arrow key.")

        if self.down_flag:
            print("Down arrow key.")

    def _check_keyup(self):
        if self.event.key == pygame.K_LEFT:
            self.left_flag = False

        if self.event.key == pygame.K_RIGHT:
            self.right_flag = False

        if self.event.key == pygame.K_UP:
            self.up_flag = False

        if self.event.key == pygame.K_DOWN:
            self.down_flag = False


if __name__ == "__main__":
    k = Keys()
    k.check_keys()

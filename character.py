import pygame


class Character:
    def __init__(self, main):
        self.main = main
        self.screen = main.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("images/spaceship.png")
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.right_flag = False
        self.left_flag = False
        self.up_flag = False
        self.down_flag = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update_ship(self):
        if self.up_flag and self.rect.top > 0:
            self.y -= 1.5
        if self.down_flag and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1.5
        if self.right_flag and self.rect.right < self.screen_rect.right:
            self.x += 1.5
        if self.left_flag and self.rect.left > 0:
            self.x -= 1.5

        self.rect.x = self.x
        self.rect.y = self.y

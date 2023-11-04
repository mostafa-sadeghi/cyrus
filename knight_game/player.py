from pygame.sprite import Sprite
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT
        self.rect.centerx = SCREEN_WIDTH/2

        self.lives = 3
        self.velocity = 5

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 100:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT - 100:
            self.rect.y += self.velocity
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.velocity

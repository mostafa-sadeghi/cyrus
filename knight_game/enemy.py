import random
from pygame.sprite import Sprite
from constants import *


class Enemy(Sprite):
    def __init__(self, x, y, image, monster_type):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = monster_type
        self.x_dir = 1
        self.y_dir = 1

        self.velocity = random.randint(1, 5)

    def update(self):
        self.rect.x += self.x_dir * self.velocity
        self.rect.y += self.y_dir * self.velocity
        if self.rect.bottom >= SCREEN_HEIGHT - 100 or self.rect.top <= 100:
            self.y_dir *= -1

        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.x_dir *= -1

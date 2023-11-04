import pygame
from constants import *
from enemy import Enemy
from player import Player
from random import randint
pygame.init()
main_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("knight game")
clock = pygame.time.Clock()

my_player = Player()
level_number = 0
enemy_group = pygame.sprite.Group()

all_enemies_images = []
for i in range(1, 5):
    all_enemies_images.append(pygame.image.load(f'assets/enemy_{i}.png'))


def start_new_level():
    global level_number
    level_number += 1
    for i in range(4):
        enemy_group.add(
            Enemy(
                randint(0, SCREEN_WIDTH-all_enemies_images[i].get_width()),
                randint(100, SCREEN_HEIGHT -
                        (100 + all_enemies_images[i].get_height())),
                all_enemies_images[i],
                i
            )
        )


def draw():
    pygame.draw.rect(main_surface, (255, 255, 255),
                     (0, 100, SCREEN_WIDTH, SCREEN_HEIGHT-200), 4)


start_new_level()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main_surface.fill((0, 0, 0))
    draw()
    my_player.draw(main_surface)
    my_player.move()
    enemy_group.draw(main_surface)
    enemy_group.update()
    pygame.display.update()
    clock.tick(FPS)

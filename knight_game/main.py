import pygame
from pyscreeze import center
from constants import *
from enemy import Enemy
from player import Player
from random import randint,choice
pygame.init()
main_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("knight game")
clock = pygame.time.Clock()

my_player = Player()
level_number = 0
score = 0
enemy_group = pygame.sprite.Group()

all_enemies_images = []
for i in range(1, 5):
    all_enemies_images.append(pygame.image.load(f'assets/enemy_{i}.png'))


def start_new_level():
    global level_number
    level_number += 1
    my_player.warp_counter += 1
    for level in range(level_number):
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


target_enemy_type = randint(0, 3)
target_enemy_image = all_enemies_images[target_enemy_type]

font = pygame.font.Font('assets/AttackGraffiti.ttf',32)



def draw():
    score_text = font.render(f'Score:{score}', True, (240,10,190))
    score_rect = score_text.get_rect(topleft=(0,10))
    lives_text = font.render(f'lives:{my_player.lives}', True, (240,10,190))
    lives_rect = lives_text.get_rect(topleft=(0,50))
    warp_text = font.render(f'warp:{my_player.warp_counter}', True, (240,10,190))
    warp_rect = warp_text.get_rect(topright=(SCREEN_WIDTH,10))
    level_text = font.render(f'level:{level_number}', True, (240,10,190))
    level_rect = level_text.get_rect(topright=(SCREEN_WIDTH,50))
    main_surface.blit(score_text,score_rect)
    main_surface.blit(lives_text,lives_rect)
    main_surface.blit(warp_text,warp_rect)
    main_surface.blit(level_text,level_rect)
    pygame.draw.rect(main_surface, (255, 255, 255),(0, 100, SCREEN_WIDTH, SCREEN_HEIGHT-200), 4)
    main_surface.blit(target_enemy_image, target_enemy_image.get_rect(centerx=SCREEN_WIDTH/2, bottom=100))


def choose_enemy_target():
    global target_enemy_type, target_enemy_image
    target_enemy_type = choice(enemy_group.sprites()).type
    
    target_enemy_image = all_enemies_images[target_enemy_type]


def check_collisions():
    global score
    collided_monster = pygame.sprite.spritecollideany(my_player, enemy_group)
    if collided_monster:
        if collided_monster.type == target_enemy_type:
            collided_monster.kill()
            score += 1
            if len(enemy_group) == 0:
                start_new_level()
            else:
                choose_enemy_target()
        else:
            my_player.reset()
            my_player.lives -= 1
            if my_player.lives <= 0:
                game_over()



def game_over():
    global running,score,level_number
    game_over_text = font.render("Game Over\nPress Enter to play again", True, (240,10,178))
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    main_surface.fill((0,0,0))
    main_surface.blit(game_over_text,game_over_rect)
    pygame.display.update()

    score = 0
    my_player.lives = 3
    level_number = 0
    enemy_group.empty()
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    paused = False
                    start_new_level()

            if event.type == pygame.QUIT:
                paused = False
                running = False

    
            


start_new_level()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_player.warp()

    check_collisions()

    main_surface.fill((0, 0, 0))
    draw()
    my_player.draw(main_surface)
    my_player.move()
    enemy_group.draw(main_surface)
    enemy_group.update()
    pygame.display.update()
    clock.tick(FPS)

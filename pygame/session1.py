import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Images!")

sound1 = pygame.mixer.Sound("sound_1.wav")
sound2 = pygame.mixer.Sound("sound_2.wav")

# sound1.play()
# pygame.time.delay(1000)
# sound2.play()

pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1, 0.0)


dragon_left_image = pygame.image.load("dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0, 0)

dragon_right_image = pygame.image.load("dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)


dragon_image = pygame.image.load('dragon_right.png')
dragon_image_rect = dragon_image.get_rect()
dragon_image_rect.centerx = WINDOW_WIDTH//2
dragon_image_rect.bottom = WINDOW_HEIGHT

VELOCITY = 30
# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_image_rect.x -= VELOCITY
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dragon_image_rect.x += VELOCITY
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dragon_image_rect.y -= VELOCITY
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                dragon_image_rect.y += VELOCITY
    display_surface.fill((0, 0, 0))
    # Blit (copy) a surface object at the given coordinates to our display
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)
    display_surface.blit(dragon_image, dragon_image_rect)

    pygame.draw.line(display_surface, (255, 255, 255),
                     (0, 75), (WINDOW_WIDTH, 75), 4)

    # Update the display
    pygame.display.update()

# End the game
pygame.quit()

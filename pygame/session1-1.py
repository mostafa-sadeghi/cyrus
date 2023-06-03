import pygame

# Initialize pygame
pygame.init()

# Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

display_surface = pygame.display.set_mode((WINDOW_WIDTH,
                                           WINDOW_HEIGHT))
pygame.display.set_caption("Our first game!")

dragon_left_image = pygame.image.load("dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0, 0)

dragon_right_image = pygame.image.load("dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)
pygame.draw.line(display_surface, (255, 255, 255),
                 (0, 75), (WINDOW_WIDTH, 75), 4)


system_font = pygame.font.SysFont('comicsansms', 64)
system_text = system_font.render(
    'Dragon Game!', True, (0, 255, 0), (10, 20, 50))
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)


custom_font = pygame.font.Font('AttackGraffiti.ttf', 32)
custom_text = custom_font.render('Dragon', True, (0, 255, 0))
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 100)

# The main game loop
running = True
while running:
    # Loop through a list of event objects that have occured
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text, custom_text_rect)

    pygame.display.update()
pygame.quit()

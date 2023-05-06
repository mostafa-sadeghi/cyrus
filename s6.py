import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
ORANGE = (214, 152, 9)
SIZE = (700, 500)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

pos_x = 0
pos_y = 0
pos_x_change = 1
pos_y_change = 1
done = True
# Main Program Loop
while done:
    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:

                done = False

            print("User pressed a key...")

        # elif event.type == pygame.KEYUP:
        #     print("User released a key...")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")

    # First, clear the screen to White.
    # screen.fill(WHITE)
    # Game logic should go here

    # Drawing code should go here
    # pygame.draw.rect(screen, ORANGE, [0, 0, 10, 10])
    pygame.draw.ellipse(screen, ORANGE, [pos_x, pos_y, 10, 10])
    pos_x += pos_x_change
    pos_y += pos_y_change

    if pos_y > 490 or pos_y < 0:
        pos_y_change = -1 * pos_y_change
    if pos_x > 690 or pos_x < 0:
        pos_x_change = -1 * pos_x_change

    # Go ahead and Update the screen
    pygame.display.flip()

    # Limit to 60 frames per second

    clock.tick(600)
pygame.quit()

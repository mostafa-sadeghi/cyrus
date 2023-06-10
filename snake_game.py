from turtle_utils import make_surface, make_turtle, change_food_position, move_snake
from time import sleep
main_surface = make_surface('blue', 'Snake Game',
                            (600, 600))
main_surface.tracer(0)

snake_head = make_turtle("square", "black")
snake_head.direction = "up"
move_snake(snake_head)


food = make_turtle("circle", "red")
food.goto(change_food_position())

running = True
while running:
    main_surface.update()
    move_snake(snake_head)
    sleep(0.2)

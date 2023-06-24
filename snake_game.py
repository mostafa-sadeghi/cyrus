from turtle_utils import *
from time import sleep

score = 0


def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"


def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"


def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"


def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"


def reset():
    global score
    score = 0
    snake_head.home()
    snake_head.direction = ""
    for body in snake_bodies:
        body.hideturtle()

    snake_bodies.clear()


main_surface = make_surface('blue', 'Snake Game',
                            (600, 600))
main_surface.tracer(0)

snake_head = make_turtle("square", "black")
snake_head.direction = "none"
food = make_turtle("circle", "red")
food.goto(change_food_position())

score_turtle = make_turtle("square", "white")
score_turtle.hideturtle()
score_turtle.goto(0, 260)

main_surface.listen()
main_surface.onkeypress(go_up, "Up")
main_surface.onkeypress(go_down, "Down")
main_surface.onkeypress(go_left, "Left")
main_surface.onkeypress(go_right, "Right")

snake_bodies = []
running = True
while running:
    main_surface.update()
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", align="center", font=52)

    if snake_head.distance(food) < 20:
        food.goto(change_food_position())
        score += 1
        new_tail = make_turtle("square", "grey")
        snake_bodies.append(new_tail)
    
    for i in range(len(snake_bodies) - 1, 0, -1):
        xpos = snake_bodies[i-1].xcor()
        ypos = snake_bodies[i-1].ycor()
        snake_bodies[i].goto(xpos,ypos)

    if len(snake_bodies)>0:
        xhead = snake_head.xcor()
        yhead = snake_head.ycor()
        snake_bodies[0].goto(xhead, yhead)


    if snake_head.xcor() > 290 or \
            snake_head.xcor() < -290 or \
            snake_head.ycor() > 230 or\
            snake_head.ycor() < -290:
        reset()

    move_snake(snake_head)

    for body in snake_bodies:
        if body.distance(snake_head) < 20:
            reset()

    sleep(0.2)

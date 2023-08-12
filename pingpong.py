from turtle import Turtle, Screen

main_surface = Screen()
main_surface.title("Ping-pong Game")
main_surface.bgcolor("grey")
main_surface.setup(width=1050, height=650)


def make_turtle(tshape, tcolor, wid, len):
    my_turtle = Turtle()
    my_turtle.speed("fastest")
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.shapesize(wid, len)
    my_turtle.penup()
    return my_turtle


left_paddle = make_turtle("square", "red", 6, 2)
left_paddle.goto(-400, 0)

right_paddle = make_turtle("square", "blue", 6, 2)
right_paddle.goto(400, 0)

ball = make_turtle("circle", "black", 1, 1)
ball.home()
ball.dx = 5
ball.dy = -5

left_player_score = 0
right_player_score = 0


score_board = make_turtle('square', "blue", 2, 2)
score_board.penup()
score_board.hideturtle()
score_board.goto(0, 260)
score_board.write("Left Player : 0    Right Player: 0",
                  align="center", font=("Courier", 24, "normal"))


def paddle_left_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)


def paddle_left_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)


def paddle_right_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)


def paddle_right_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)


main_surface.listen()
main_surface.onkeypress(paddle_left_down, "s")
main_surface.onkeypress(paddle_left_up, "w")
main_surface.onkeypress(paddle_right_down, "Down")
main_surface.onkeypress(paddle_right_up, "Up")


running = True
while running:
    main_surface.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 500:
        ball.home()
        ball.dy *= -1
        left_player_score += 1
        score_board.clear()
        score_board.write(f"Left Player : {left_player_score}    Right Player: {right_player_score}",
                          align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -500:
        ball.home()
        ball.dy *= -1
        right_player_score += 1
        score_board.clear()
        score_board.write(f"Left Player : {left_player_score}    Right Player: {right_player_score}",
                          align="center", font=("Courier", 24, "normal"))

    if (ball.xcor() > 360 and ball.xcor() < 370) \
        and (ball.ycor() < right_paddle.ycor() + 40 and
             ball.ycor() > right_paddle.ycor()-40):
        ball.setx(360)
        ball.dx *= -1

    if (ball.xcor() < -360 and ball.xcor() > -370) \
        and (ball.ycor() < left_paddle.ycor() + 40 and
             ball.ycor() > left_paddle.ycor()-40):
        ball.setx(-360)
        ball.dx *= -1

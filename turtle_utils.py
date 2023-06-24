from turtle import Screen, Turtle
from random import randrange


def make_surface(color, title, size):
    display_surface = Screen()
    display_surface.bgcolor(color)
    display_surface.title(title)
    display_surface.setup(width=size[0], height=size[1])
    return display_surface


def make_turtle(turtle_shape, turtle_color):
    turtle_object = Turtle()
    turtle_object.shape(turtle_shape)
    turtle_object.color(turtle_color)
    turtle_object.speed("fastest")
    turtle_object.penup()
    return turtle_object


def change_food_position():
    food_x = randrange(-270, 270)
    food_y = randrange(-270, 210)
    return food_x, food_y


def move_snake(snake):
    if snake.direction == "up":
        yposition = snake.ycor()
        snake.sety(yposition + 20)
    if snake.direction == "down":
        yposition = snake.ycor()
        snake.sety(yposition - 20)
    if snake.direction == "right":
        xposition = snake.xcor()
        snake.setx(xposition + 20)
    if snake.direction == "left":
        xposition = snake.xcor()
        snake.setx(xposition - 20)


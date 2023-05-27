import turtle
COLORS = ("red", "green", "blue")


def my_func(x, y):
    pen.right(40)
    pen.begin_fill()
    for i in range(5):
        pen.pencolor(COLORS[i % 3])
        pen.forward(100)
        pen.right(144)

    pen.end_fill()


screen = turtle.Screen()
screen.bgcolor('orange')
pen = turtle.Turtle()
pen.shape('turtle')
pen.shapesize(2)
pen.color("red", "cyan")
pen.pensize(4)
pen.penup()
pen.goto(-50, 0)
pen.pendown()
pen.onclick(my_func)


# pen.penup()
# pen.goto(-50, 150)
# pen.write("Our nice star", font=("Arial", 18, "bold"))
# pen.hideturtle()
turtle.done()

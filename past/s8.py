# def my_func():
#     print("somthing")

# my_func()

# def add(x,y):
#     return x + y

# result = add(2,3)
# print(f"2 + 3 = {result}")

# sub   mul    div


import turtle

COLORS = ("red", "green", "purple")
screen = turtle.Screen()
screen.bgcolor('orange')
my_pen = turtle.Turtle()

my_pen.shape('turtle')
my_pen.color("red", "cyan")
my_pen.pensize(4)
my_pen.shapesize(3)

my_pen.begin_fill()
for i in range(3):
    my_pen.pencolor(COLORS[i])
    my_pen.forward(100)
    my_pen.left(120)
my_pen.end_fill()

my_pen.penup()
my_pen.goto(-100, 200)
while True:
    my_pen.left(15)

turtle.done()

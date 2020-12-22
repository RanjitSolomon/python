# https://docs.python.org/3/library/turtle.html
#   Turtle Colors
# https://cs111.wellesley.edu/labs/lab01/colors
# https://docs.python.org/3/library/turtle.html#turtle.color
#   Trinket Turtle colors
# https://trinket.io/docs/colors
#    Random Walk
# https://en.wikipedia.org/wiki/Random_walk

import random
# import Turtle
from turtle import Screen
import turtle as t
# from turtle import *
# import turtle as T

tim = t.Turtle()
tim.shape("turtle")  # Other shapes "arrow", "turtle", "circle", "square", "triangle", "classic"
tim.color('red')

# Draw a square
for _ in range(4):
    tim.forward(100)
    tim.left(90)

# Draw a dashed line
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

# Draw a triangle
for _ in range(3):
    tim.right(120)
    tim.forward(100)

for _ in range(4):
    tim.right(90)
    tim.forward(100)

for _ in range(5):
    tim.right(72)
    tim.forward(100)

for _ in range(6):
    tim.right(60)
    tim.forward(100)

tim.penup()
tim.setx(-400)
tim.pendown()
x = 3
y = 4
for _ in range(y):
    for _ in range(x):
        tim.right(360/x)
        tim.forward(100)
    x += 1

tim.penup()
tim.sety(400)
tim.pendown()
# Angela's Solution
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 12):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

# Random walks
tim.penup()
tim.setx(0)
tim.sety(0)
tim.pendown()
tim.pensize(5)
for _ in range(100):
    r = random.randint(0, 1)
    if r == 0:
        tim.right(90)
    else:
        tim.left(90)
    tim.color(random.choice(colours))
    tim.speed(random.randint(5, 10))
    tim.forward(10)

tim.penup()
tim.setx(100)
tim.sety(100)
tim.pendown()
# Angela's solution
t.colormode(255)
directions = [0, 90, 180, 270]

tim.pensize(15)
tim.speed("fastest")


def random_color():
    red = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (red, g, b)
    return rgb


for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

# Spirograph
tim.pensize(2)
tim.speed(10)
for i in range(6):
    for color in ('red', 'magenta', 'blue', 'cyan', 'green', 'yellow'):
        tim.color(color)
        tim.circle(100)
        tim.left(10)
    tim.hideturtle()

tim.penup()
tim.setx(100)
tim.sety(100)
tim.pendown()
# Angela's solution


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
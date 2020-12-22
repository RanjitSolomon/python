import colorgram
import turtle
from turtle import Screen
import random

# rgb_colors = []
# colors = colorgram.extract("pic.jpg", 10)

# for color in colors:
#    # rgb_colors.append(color.rgb)
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)

# print(rgb_colors)
color_list = [(175, 74, 42), (211, 162, 14), (239, 214, 96), (4, 102, 159), (173, 44, 65), (25, 42, 73), (213, 229, 235), (128, 178, 196)]

height = turtle.window_height()   # 1080
weight = turtle.window_width()    # 1280

turtle.penup()
turtle.hideturtle()
turtle.setx(-620)
turtle.sety(520)
turtle.colormode(255)
turtle.speed("fastest")

for i in range(14):
    y = 80
    for j in range(16):
        turtle.pendown()
        turtle.dot(40, random.choice(color_list))
        turtle.penup()
        turtle.forward(80)

    turtle.setx(-620)
    turtle.sety(520 - ((i + 1) * y))

# Angela's solution
tim = turtle.Turtle()
tim.home()
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

# y_pos = [-70, -40, -10, 20, 50, 80]
y_cor = 100
for i in range(6):
    y_cor -= 25
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_cor)
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

winning_color = ""
while is_race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() >= 235:
            winning_color = turtle.pencolor()
            is_race_on = False
            print(winning_color)
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner")
            else:
                print(f"You've lost! The {winning_color} is the winner")

screen.exitonclick()
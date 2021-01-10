from turtle import Turtle, Screen
from snake import Snake
import time
# Create a snake body
# Move the snake
# Create snake food
# Detect collision with food
# Create a scoreboard
# Detect collision with wall
# Detect collision with tail(body?)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# turtle 20 x 20  screen 600 x 600
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()

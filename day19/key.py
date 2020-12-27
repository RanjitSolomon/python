from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()

screen.listen()


def move_fwd():
    tim.fd(10)


def move_bck():
    tim.bk(10)


def turn_left():
    tim.setheading(tim.heading() + 10)


def turn_right():
    tim.setheading(tim.heading() - 10)


def screen_clear():
    tim.reset()


screen.onkeypress(move_fwd, "w")
screen.onkeypress(move_bck, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(screen_clear, "c")


screen.exitonclick()
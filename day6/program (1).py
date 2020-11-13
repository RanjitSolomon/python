def turn_right():
    turn_left()
    turn_left()
    turn_left()
   
while not at_goal():
    if (wall_on_right() and not wall_in_front()) and not right_is_clear():
        move()
    elif wall_in_front() and not right_is_clear():
        turn_left()
    elif right_is_clear():
        turn_right()
        move()
        turn_right()
        move()
        
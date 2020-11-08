import random
# random.randint0,9)
opt1 = round(random.uniform(0,1))
opt2 = round(random.uniform(0,1))
opt3 = round(random.uniform(0,2))

print(opt1, opt2, opt3)

print("Welcome to Treassure Island. \n Your missing is to find the treasure\n")
decision1 = (input("Which way would you like to turn (Left or Right) L R \n")).lower()

direction1 = 0
if decision1 == "l":
    direction1 = opt1
else:
    direction1 = (1 - opt1)

print(direction1)

if direction1 == 0:
    print("Game Over")
else:
    decision2 = (input("Would you want to swim or wait s or w \n")).lower()
    direction2 = 0
    if decision2 == "s":
        direction2 = opt2
    else:
        direction2 = 1 - opt2

    if direction2 == 0:
        print("Game Over")

    else:
        decision3 = (input("Select a door Red, Blue Yellow  r or b or y \n")).lower()
        direction3 = 0
        if decision3 == "r":
            direction3 = opt3
        elif direction3 = "b":
            direction3 = 1 - opt3
        else:
            










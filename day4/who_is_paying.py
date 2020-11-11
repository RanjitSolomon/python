import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method  - askpython.com "split"
namesAsCSV = input("Give me everybody's names, seprated by comma \n")
names = namesAsCSV.split(", ")

rand_num = random.randint(0, len(names)-1)
print(rand_num)
print(f"{names[rand_num]} is going to buy the meal today!")

# askpython - choice
print(f"{random.choice(names)} will be paying as per second method")
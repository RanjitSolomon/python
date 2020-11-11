import  my_module
import random

print(my_module.pi)
print(random.randint(1,10))

print(random.random())  # random number between 0 and 1

print(random.random() * 5)  # number between 0 to 4.999999

love_score = random.randint(1,100)
print(f"your love score is {love_score}")


# Coin Toss
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

coin_toss = random.randint(0,1)
if (coin_toss):
    print("Head")
else:
    print("Tails")


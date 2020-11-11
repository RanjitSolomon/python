#  Rock wins against Scissors
# Scissors win against Paper
# Paper wins against Rock
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

your_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper  or 2 for Scissors \n"))
choices = [rock, paper, scissors]

your_choice = choices[your_input]
print("Your choice \n")
print(your_choice)

computer_input = random.randint(0,2)
computer_choice = choices[computer_input]
print("Computer Choice\n")
print(computer_choice)

if your_input == 0 and computer_input == 2:
    print("you win")
elif computer_input == 0 and your_input ==2:
    print("You lose")
elif computer_input > your_input:
    print("You Lose")
elif your_input > computer_input:
    print("You win")
elif computer_input == your_input:
    print("It is a draw")






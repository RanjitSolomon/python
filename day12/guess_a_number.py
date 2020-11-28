from clear_sys import clear
from art import logo
import random

clear()
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. ")
guess_number = random.randint(1,100)
print(f"Pssst, the correct answer is {guess_number}")
difficulty_level = input("Choose a difficulty Type 'e' easy or 'h' hard: ")

if difficulty_level == "e":
    no_of_chances = 10
elif difficulty_level == "h":
    no_of_chances = 5

print(f" you have {no_of_chances} attempts remaining to guess he number ")

while no_of_chances:
    guess = int(input("Make a guess: "))
    no_of_chances -= 1
    if guess > guess_number:
        print("Too High")
    elif guess < guess_number:
        print("Too Low")
    elif guess == guess_number:
        print(f"You got it! The answer was {guess_number} ") 
        break       
    print(f"You have {no_of_chances} attempts remaining to guess the number")

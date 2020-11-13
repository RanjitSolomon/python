#  https://en.wikipedia.org/wiki/Hangman_(game)
# https://hangmanwordgame.com/?fca=1&success=0#/
# https://developers.google.com/edu/python/lists#for-and-in

import random 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable 
# called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable 
# called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in 
# the chosen_word.

chosen_word = random.choice(word_list)
print(chosen_word)
print(len(chosen_word))
len_word = len(chosen_word)

guess = (input("Please guess a word")).lower()

answer =""

for i in range(len_word -1):
    if guess == chosen_word[i]:
        print("Right")
        answer += " " + guess + " "
    else:
        print("wrong")
        answer += " _ "

print(answer)

print(" Second Method ")

display = ["_"] * len(chosen_word)
print(display)

for pos in range(len_word):
    letter = chosen_word[pos]
    if letter == guess:
        print("Right")
        display[pos] = letter

    else:
        print("Wrong")

print(display)

import random
import clear_sys
from sketch import stages, logo
from hangman_words import word_list

clear_sys.clear()

# word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
# Test
print(chosen_word)

lives = 6
word_length = len(chosen_word)
display = ['_'] * word_length

end_of_game = False

while not end_of_game:
    
    clear_sys.clear()
    print(logo)
    print(stages[lives])
    print(chosen_word)
    print(f"{' '.join(display)}")
    guess = (input("Please guess a letter   ")).lower()
    if guess in display:
        print(f"You've already guessed {guess}")

    for pos in range(word_length):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True 
            print("You lose.")


    if "_" not in display:
        end_of_game = True
        print(f"{'You win! you guessed the word '.join(display)}")
 
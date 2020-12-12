from random import randint
from art import logo, vs
from game_data import data
from clear_sys import clear

#print(logo)

game_status = True
no_of_times = 0
status_text = ""

while game_status:
    clear()
    if no_of_times == 0:
        first_item = data[randint(0,49)]

    second_item = data[randint(0,49)]
    print(logo)
    print(status_text)
    print(f"Compare A: {first_item.get('name')}, {first_item.get('description')}, {first_item.get('country')} " )
    print(vs)
    print(f"Compare B: {second_item.get('name')}, {second_item.get('description')}, {second_item.get('country')} " )
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()


    if guess == "a":
        if int(first_item.get('follower_count')) >int(second_item.get('follower_count')):
            no_of_times += 1
            status_text = f'Youre right! Current Score: {no_of_times}'
            first_item = second_item
            continue
        else:
            print(f'Sorry, Thats wrong. Final score: {no_of_times}' )
            game_status = False
    elif guess == "b":
        if int(second_item.get('follower_count')) > int(first_item.get('follower_count')):
            no_of_times += 1
            status_text = f'Youre right! Current Score: {no_of_times}' 
            first_item = second_item
            continue
        else:
            print(f'Sorry, Thats wrong. Final score: {no_of_times}' )
            game_status = False
    

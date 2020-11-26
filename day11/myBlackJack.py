from clear_sys import clear
from art import logo
import random

play_no_play =  input("Do you want to play black jack 'y' or 'n' ").lower()
is_game_over = True

if play_no_play == "y":
    is_game_over = False

while not is_game_over:
    clear()
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    comp_cards = []

    def deal_card(card):
        card.append(random.choice(cards))

    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) ==2:
            return 0

        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)

        return (sum(cards))

    for _ in range(2):
        deal_card(user_cards)
        deal_card(comp_cards)

    user_score = calculate_score(user_cards)
    comp_score = calculate_score(comp_cards)
    
    print(f" Your cards: {user_cards}, current score: {user_score} ")
    print(f" Computer's first card: {comp_cards[0]} ")

    if user_score == 0 or comp_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if user_should_deal == "y":
            deal_card(user_cards)
        else:
            is_game_over = True




    play_no_play = input("Do you want to plat another game 'y' or 'n' ").lower()
    if play_no_play == "n":
        is_game_over = True


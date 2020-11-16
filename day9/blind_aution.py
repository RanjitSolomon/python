from clear_sys import clear
from art import logo
# from clear_sys import clear


#HINT: You can call clear() to clear the output in the console.
clear()
# logo()

print("Welcome to the secret auction program \n")

yes_no = True
auction = {}

while yes_no:
    name = input("What is your name?:  ")
    bid = input("What's your  bid?: $")
    yes_no = input("Are there are any other bidders? Type 'y' or 'n' : ").lower()

    auction[name] = bid

    if yes_no == "n":
        yes_no = False
    else:
        clear()

print(auction)

winner = ""
high_value = 0.0
for a in auction:
    if float(auction[a]) > high_value:
        high_value = float(auction[a])
        winner = a
        print(high_value)
        
print(f"The winner is {winner} with a bid of ${high_value} ")





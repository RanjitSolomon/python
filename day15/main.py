machine_on = True
water = 100
coffee = 76
milk = 50
cash = 2.5

def resource(type):
    if type == "e":
        if water < 50:
            print("Sorry, there is not enough water. ")
            return False
        if coffee < 18:
            print("Sorry, there is not enough coffee")
            return False
    elif type == "l":
        if water < 200:
            print("Sorry, there is not enough water")
            return False
        if coffee < 24:
            print("Sorry, there is not enough coffee")
            return False
        if milk < 150:
            print("Sorry, there is not enough milk")
            return False
    elif type == "c":
        if water < 250:
            print("Sorry, there is not enough water")
            return False
        if coffee < 24:
            print("Sorry, there is not enough coffee")
            return False
        if milk < 100:
            print("Sorry, there is not enough milk")
            return False
    return True

def money(coffee_order):
    global cash
    quarters = int(input("Enter how many quarters: "))
    dimes = int(input("Enter how many dimes: "))
    nickels = int(input("Enter how many nickels: "))
    pennies = int(input("Enter how many pennies: "))

    money_received = .25 * quarters + .10 * dimes + .05 * nickels + .01 * pennies
    print(money_received)
    if coffee_order == "e":
        if money_received > 1.50:
            print(f"Here is your change ${money_received - 1.50} ")
            cash += 1.50
            return True
        elif money_received == 1.50:
            print("Thank you for your order")
            cash += 1.50
            return True
        elif money_received < 1.50:
            print("Sorry, that's not enough money. Money refunded")
            return False
    elif coffee_order == "l":
        if money_received > 2.50:
            print(f"Here is your change ${money_received - 2.50} ")
            cash += 2.50
            return True
        elif money_received == 2.59:
            print(f"Thank you for your order")
            cash += 2.50
            return True
        elif money_received < 2.50:
            print("Sorry, that's not enough money. Money refunded")
            return False
    elif coffee_order == "c":
        if money_received > 3.00:
            print(f"Here is your change ${money_received - 3.00} ")
            cash += 3.00
            return True
        elif money_received == 3.00:
            cash += 3.00
            print(f"Thank you for your order")
            return True
        elif money_received < 3.00:
            print(f"Sorry, that's not enough money. Money Refunded")
            return False

def make_coffee(type):
    global water
    global coffee
    global milk
    if type == "e":
        water -= 50
        coffee -= 18
    elif type == "l":
        water -= 200
        coffee -= 24
        milk -= 150
    elif type == "c":
        water -= 250
        coffee -= 24
        milk -= 100


while machine_on:
    print("Espresso - $1.50, Latte - $2.50, Cappuccino - $3.00")
    coffee_input = input("What would you like? (e - espresso, l - latte, c - cappuccino)").lower()
    if coffee_input  == "off":
        machine_on = False
        continue
    elif coffee_input == "report":
        print(f"water = {water}, coffee = {coffee}, milk = {milk}, money = ${cash}")
        continue

    coffee_order = coffee_input[0];
    print(coffee_order);
    if coffee_order != "e" and coffee_order != "l" and coffee_order != "c":
        print("Invalid selection, Please select Espresso, latte, or cappuccino")
        continue
    
    if resource(coffee_order):
        if money(coffee_order):
            make_coffee(coffee_order)
            if coffee_order == "e":
                print("Here is your expresso. Enjoy!")
            elif coffee_order == "l":
                print("Here is your latte. Enjoy!")
            elif coffee_order == "c":
                print("Here is your cappuccino. Enjoy!")

    
    #machine_on = False;
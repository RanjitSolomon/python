MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def check_resources(ingredients):
    global resources
    for item in ingredients:
        if int(resources[item]) < int(ingredients[item]):
            print(f" Sorry There is not enough {item} ")
            return False
    return True


def payment_process(price):
    payment = int(input("Enter the Quarters: ")) * 0.25
    payment += int(input("Enter the dimes: ")) * 0.10
    payment += int(input("Enter the nickels: ")) * 0.05
    payment += int(input("Enter the pennies: ")) * 0.01

    if payment > price:
        global profit
        print(f"Here is ${payment - price} in change.")
        profit += price
        return True
        return True
    elif payment == price:
        profit += price
        return True
    elif payment < price:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(coffee):
    global resources
    for item in coffee:
        resources[item] -= coffee[item]
    return True


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice != "espresso" and choice != "latte" and choice != "cappuccino" and choice  != "off" and choice != "report":
        print("Invalid Selection")
        continue
    elif choice == "off":
        print("Coffee Machine Turned Off")
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']} ")
        print(f"Water: {resources['milk']} ")
        print(f"Water: {resources['coffee']} ")
        print(f"Money: ${profit} ")
    else:
        drink = MENU[choice]
        if check_resources(drink['ingredients']):
            if payment_process(drink['cost']):
                if make_coffee(drink['ingredients']):
                    print(f"Here is your {choice}. Enjoy!")
from datetime import date, datetime

def greet(name, loc):
    print(f"Hello {name} in {loc}")
    print(f"Today's date is {date.today()} ")
    print(f"Current date and time is {datetime.now()} ")

name = input("What is your name? \n")
location = input("What is your location? \n")
greet(name, location)

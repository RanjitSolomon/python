print("Welcome to the rollercoaster\n")
height = int(input("What is your height in cm? \n"))

if height >= 120:
    print(" You can ride the rollercoaster")
    age = int(input("What is your age \n"))
    if age > 18:
        print("The ticket price is 12")
    elif age > 12:
        print("The ticket price is 7")
    else:
        print("The ticket price is 5")
else:
    print("Sorry, you have to grow taller before you can ride.")
# operator
# >
# <
# >=
# <= 
# ==
# !=
# % modulo 7 % 2 = 1

# Odd or Even
odd_even = int(input("Enter a number \n"))
if odd_even % 2 == 0:
    print(f"the number {odd_even} is a even number")
else:
    print(f"the number {odd_even} is a odd number")

# BMI Calculator
# Under 18.5 they are underweight
# Over 18.5  but below 25 they have a normal weight
# Over 25 but below 30 they are overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese

height = float(input("Please enter your height for BMI calculation \n"))
weight = float(input("Please enter your weight \n"))

bmi = round(weight / height**2,1)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, You are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, You are normal weight")
elif bmi < 39:
    print(f"Your bmi is {bmi}, You are obese")
else:
    print(f"Your bmi is {bmi}, You are clinically obese") 

# Leap Year
# Every year that is evenly divisible by 4
#   Except every year that is evenly divisible by 100
#       unless the year is also evenly divisible by 400\
leap_year = int(input("Enter a year to find out if it is a leap year \n"))

if leap_year % 4 != 0 :
    print(f"Year {leap_year} is not a leap year")
else:
    if leap_year % 100 != 0:
        print(f"Year {leap_year} is  a leap year")
    else:
        if leap_year % 400 == 0:
            print(f"Year {leap_year} is a leap year")
        else:
            print(f"Year {leap_year} is not a leap year")

# Pizza Order
# Small Pizza 15
# medium Pizza 20
# Large Pizza 25
# Pepperoni for small pizza +2
# peppernoi for medium or large pizza +3
# Extra cheese for any size pizza +1
size_of_pizza  = input("Enter the size of pizza enter  S M L\n")
add_pep = input("Do you want to add pepperoni? Y N \n")
add_cheese = input("Do you want to add extra cheese? Y N \n")

if size_of_pizza =="s":
    price = 15
elif size_of_pizza == "m":
    price = 20
elif size_of_pizza =="l":
    price = 25

if add_pep == "y":
    if size_of_pizza == "s":
        price = price + 2
    else:
        price = price + 3

if add_cheese == "y":
    price = price + 1

print(f"Your final bill is ${price}.")  


# Logical Operator
# A and B           T and T   is T, 
# A or B            F and F    is F
# not

# Love Calculator
name1 = (input("Enter fhe frirst name for the love calculator\n")).lower()
name2 = (input("Enter the second name for the love calculator\n")).lower()
name = name1 + name2
total1 = 0
total2 = 0

total1 = total1 + name.count("t")
total1 = total1 + name.count("r")
total1 = total1 + name.count("u")
total1 = total1 + name.count("e")

print(total1)

total2 = total2 + name.count("l")
total2 = total2 + name.count("o")
total2 = total2 + name.count("v")
total2 = total2 + name.count("e")

print(total2)
total = str(total1) + str(total2)
print(total)

if ((total1) < 10 ) or ((total) > 90):
    print(f"Your love score is {total}, you go together like coke and menthol ")
elif ((total) >= 40) and ((total) <= 50 ):
    print(f"Your love score is {total}, you are alright together")
else:
    print(f"Your score is {total}")













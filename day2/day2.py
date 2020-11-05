# Python primitive Data Types

# String
print("String Addition: " + "123" + "345")

# Integer
print("Integer Addition: " + str(123 + 345))
print("Replace comma with underscore: " + str(123_456 + 345_678))

# Float
print("Float Addition: " + str(123.12 + 345.67))

# Boolean
print(True)
print(False)

# 17. Type Error, Type Checking and Type Conversion
# check ype
# num_char = len(input("What is your name"))
int_type = 6
print(type(int_type))

str_type = "Hello"
print(type(str_type))

flt_type = 123.12
print(type(flt_type))


# type conversion
print("the nunber of char " + str(int_type))

print(70 + float("100.00"))

print(71 + int("100"))


# Excerse  add a two digit number
two_digit_num = input("Enter a two digit number to add \n")
print(int(two_digit_num[0]) + int(two_digit_num[1]))

# Mathematical operators
print(3 + 5)
print(7 - 4)
print(3 * 2)
print(6/3)
print(type(6/3))   # float
print(6//3)
print(type(6//3))  # int
print(2 **3)        # 2 x 2 x 2 = 8

# PEMDAS
# Parentheses           ()
# Exponents             **
# Multiplication        * /
# Division  
# Addition              + - 
# Subraction

print(3 * 3 + 3 / 3 - 3)    # LR  answer: 7
print(3 * (3 + 3) / 3 - 3)


# BMI Calculator
# BMI   = weight / height * height

weight = input("Enter your weight in kg \n")
height = input ("Enter your height in m \n")

print ( "Your BMI is " + str(float(weight)//float(height)**2))



# Number manipulation and F strings in Python
print("8/3 is rounded " + str(round(8/3)))
print(("8/3 is rounded to 2 decimal " + str(round(8/3))))
print(8 // 3)   # floor division - drop all after decimal


score = 0
isWinning = True

# f string

print(f"your score is {score}, your height is {height} and your winning is {isWinning}")



# life in weeks\
from datetime import date
cur_age = input("What is your current age? \n")
# to_day = date.today()
# print(to_day.month)
print(f"You have {(90 * 365) - (int(cur_age) * 365)} days, {(90 * 52 - (int(cur_age) * 52))} weeks, and {(90 - int(cur_age)) * 12} months")


# Tip Calculator
print("Welcome to the tip calculator\n")
bil = float(input("What was the total bill?"))
per = float(input("What percentage tip would you likd to give"))
peps = int(input("How many people to split the bill?"))

print(f"Each person should pay: {round((bil + bil * per/100)/peps, 2)}")

















































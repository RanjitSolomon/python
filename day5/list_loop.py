import random

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)

# Average Height
# student_heights = [180, 124, 165, 173, 189, 169, 146]

students_heights = input("Input a list of student heights \n").split()

print(students_heights)

total = 0
num = 0
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
    total += int(students_heights[n])
    num = n


print(round(total/(num + 1)))

total2= 0
i = 0
for stu in students_heights:
    total2 += stu
    i += 1

print(round(total2/i))

# list sum
print(round(sum(students_heights)/len(students_heights)))

student_scores = input("Input a list of student scores \n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

print(student_scores)

max_value = 0
for score in student_scores:
    if score > max_value:
        max_value = score
print(max_value)

# max and min
print(max(student_scores))

# range
for number in range(1, 11):
    print(number)

for number in range(1, 11, 2):
    print(number)

# add the sumb from 1 to 100
add_upto_100 = 0
for number in range(1, 101):
    add_upto_100 +=  number
print(add_upto_100)

# add the even number in range 1 to 100
add_upto_100 = 0
for number in range(2, 101, 2):
    add_upto_100 += number
print(add_upto_100)

add_upto_100 = 0
for number in range(1, 101):
    if number % 2 == 0:
        add_upto_100 += number
print(add_upto_100)

# FizzBuzz
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number %3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


# PyPassword generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
pwd = [letters, numbers, symbols]
print("Welcome to the PyPassword Generator\n")
pass_char = int(input("How many letters would you like in your password\n"))
pass_sym = int(input("How many symbols would you like?\n"))
pass_num = int(input("How many numbers would you like?\n"))

pw = ""
# Eazy level
# ABCD*!123
for char in range(1, pass_char):
    pw += random.choice(letters)

for char in range(1, pass_sym):
    pw += random.choice(symbols)

for char in range(1, pass_num):
    pw += random.choice(numbers)

print("simple password generated")
print(pw)


# Hard
# x*12B!
pw = ""
for pw_item in range(1, pass_char + pass_num + pass_sym):
    row = random.randint(0,2)
    col = 0
    if row == 0:
        col = random.randint(0, pass_char - 1)
    elif row == 1:
        col = random.randint(0, pass_sym - 1)
    elif row == 2:
        col = random.randint(0, pass_num - 1)

    #print(str(row) + " " + str(col))
    pw += pwd[row][col]

print("Complex pawword generated")
print(pw)


# Angela's solution
pw_list = []
pw = ""
for char in range(1, pass_char):
    pw_list.append(random.choice(letters))

for char in range(1, pass_sym):
    pw_list += random.choice(symbols)

for char in range(1, pass_num):
    pw_list += random.choice(numbers)

print(pw_list)
print("Angela's solution")
random.shuffle(pw_list)
print(pw_list)

for char in pw_list:
    pw += char

print(pw)


pw = "".join(pw_list)
print(pw)





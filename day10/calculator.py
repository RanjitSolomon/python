from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 != 0:
        return n1/n2

operations = {
    "+": add, 
    "-": subtract, 
    "x": mul, 
    "/": div
}

f_number = int(input("Enter First Number"))
s_number = int(input("Enter Second Number"))
operation = input("Enter + - x or /")

print(f"{f_number} {operation} {s_number} = {operations[operation](f_number, s_number)}")



if operation == "+":
    print(add(f_number, s_number))
elif operation == "-":
    print(subtract(f_number, s_number))
elif operation == "x":
    print(mul(f_number, s_number))
elif operation == "/":
    print(div(f_number, s_number))
else:
    print("not ")



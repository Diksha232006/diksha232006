# Define functions for calculator
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

# User options that should be performes
print("""Enter operation to be performed
1 for add
2 for sub
3 for mul
4 for div""" )

# Take user input
d = input("Enter your choice--> ")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# function calling
if d == "1":
    print("Addition of two numbers:", add(a, b))
elif d == "2":
    print("Subtraction of two numbers:", sub(a, b))
elif d == "3":
    print("Multiplication of two numbers:", mul(a, b))
elif d == "4":
    if b != 0:
        print("Division of two numbers:", div(a, b))
    else:
        print("Cannot divide by zero!")
else:
    print("You entered a wrong operation!!!")

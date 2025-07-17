def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

print("""Enter operation to be performed
        1 for add
        2 for sub
        3 for mul
        4 for div""" )


d=input("Enter your choice-->")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))



if d == add:
    print("Addition of two numbers:", x+y)
elif d == sub:
    print("Subtraction of two numbers:", x-y)
elif d == mul:
    print("Multiplication of two numbers:", x*y)
elif d== div:
    if i != 0:
        print("Division of two numbers:", x/y)
    else:
        print("Cannot divide by zero!")

else:
    print("You entered a wrong operation!!!")


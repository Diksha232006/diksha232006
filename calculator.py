print("""Enter your operation to be performed:
       1 for addition
       2 for subtraction
       3 for multiplication
       4 for division
       5 for modulus""")

b = int(input("Enter your choice 1/2/3/4/5: "))  
d = int(input("Enter first number:-> "))
i = int(input("Enter second number:-> "))

if b == 1:
    print("Addition of two numbers:", d + i)
elif b == 2:
    print("Subtraction of two numbers:", d - i)
elif b == 3:
    print("Multiplication of two numbers:", d * i)
elif b == 4:
    if i != 0:
        print("Division of two numbers:", d / i)
    else:
        print("Cannot divide by zero!")
elif b == 5:
    print("Modulus of two numbers:", d % i)
else:
    print("You entered a wrong operation!!!")


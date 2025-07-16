
gender=int(input("""enter a gender
                 1) For Male
                 2) For female"""))
age=int(input("enter age:"))
if gender =="Male":
    if age >=21:
        print("You are eligible for marriage")
    else:
        print("you are not eligible for marriage")
elif gender == "Female":
  if age >=18:
    print("You are eligible for  marriage")
else:
    print("You are not eligible for marriage")

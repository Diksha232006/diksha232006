d=int(input("Enter total water bottels:->"))
i=int(input("Enter bottles that you drink per today:->"))
days=1
while d > 0:
    if (d>i):
        print(f"day {days}: Drank {i} Bottles. {d-i}left..")
        d-=i
    else:
        print(f"day {days}:Drank {d} Bottle{'s' if d>1 else ''}.0 left")
        days+=1
print("no bottles left")
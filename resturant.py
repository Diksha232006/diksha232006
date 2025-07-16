
total_b = float(input("Enter total bill amount: "))
m = int(input("Enter number of members for division: "))

if m <= 0:
    print("Number of friends must be greater than 0.")
else:
    tip_percent = float(input("Enter tip percent (10 to 50): "))
    if 10 <= tip_percent <= 50:
        tip_a = (total_b * tip_percent) / 100
        total_with_tip = total_b + tip_a
        per_person_amount = total_with_tip / m

        print(f"Bill amount: ₹{total_b:.2f}")
        print(f"Tip amount ({tip_percent}%): ₹{tip_a:.2f}")
        print(f"Total bill with tip: ₹{total_with_tip:.2f}")
        print(f"Each person pays: ₹{per_person_amount:.2f}")
    else:
        print("Tip percent must be between 10 and 50.")



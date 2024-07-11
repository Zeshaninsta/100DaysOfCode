print("Welcome to the tip calculator")
total = float(input("what was the total bill? $"))
tip = int(input("what percentage tip would you like to give? 10, 12, 15: "))
people = int(input("How many people to split the bill? "))

print(f"Total bill without tip = ${total}")
tip_total = tip * total / 100
print(f"Tip Amount = ${tip_total}")
all_total = tip_total + total
print(f"Total Amount with tip = ${all_total}")
total_people = all_total / people
print(f"Amount Per person = ${round(total_people, 2)}")
result = round(total_people, 2)
print(f"each person should pay: ${result}")

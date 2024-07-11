# Tip Calculation Logic
def tip_logic(tip, total, people):
    print(f"Total Bill without tip = ${total}")
    tip_amount = tip * total / 100
    print(f"Tip Amount = ${tip_amount}")
    total_amount =total + tip_amount
    print(f"Total Amount with tip = ${total_amount}")
    amount_per_person = total_amount / people
    print(f"Amount per person = ${round(amount_per_person, 2)}")
    result = round(amount_per_person, 2)
    return result

# Main Function
def main():
    print("welcome to tip calculator")
    total = float(input("what was the total bill? $"))
    tip = int(input("How much tip would you like to give? 15, 12, 10: "))
    person = int(input("How many person Split the Bill? "))
    resutl = tip_logic(tip, total, person)
    print(f"Each Person should pay ${resutl}")
    
if __name__ == "__main__":
    main()
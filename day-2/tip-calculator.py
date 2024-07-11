# creating a function

def tip_logic(people, tip, total):
    tip_total = tip * total / 100
    all_total = tip_total + total
    total_people = all_total / people
    # result = round(total_people, 2)
    return total_people

def main():
    print("Welcome to the tip calculator")
    total = float(input("what was the total bill? $"))
    tip = int(input("what percentage tip would you like to give? 10, 12, 15:  "))
    people = int(input("How many people to split the bill? "))
    result = tip_logic(people, total, tip)
    print(f"each person should pay: {result}")
    

if __name__ == "__main__":
    main()




#print("Welcome to the tip calculator")
#total = float(input("what was the total bill?"))
#tip = float(input("what percentage tip would you like to give? 10, 12, 15"))
#people = float(input("How many people to split the bill?"))

#tip_total = tip * total / 100
#all_total = tip_total + total
#total_people = all_total / people
#result = round(total_people, 2)
#print(f"each person should pay: {result}")

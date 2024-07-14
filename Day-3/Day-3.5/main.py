# Day 3.5 - Love Calculator
def love_calculator_logic(name):
    true = "true"
    love = "love"
    true_count = 0
    love_count = 0
    for letter in true:
        count = name.count(letter)
        true_count += count
        print(f"{letter} occurs {count} times")
    print(f"Total = {true_count}")
    #return true_count

    for letter in love:
        count = name.count(letter)
        love_count += count
        print(f"{letter} occurs {count} times")
    print(f"Total = {love_count}")
    result = str(true_count) + str(love_count)
    return result

# Conditions
def message_condition(result):
    if int(result) < 10 or int(result) > 90:
        return "You go together like coke and mentos"
    elif int(result) >= 40 or int(result) >= 50:
        return "You are alright together"
    else:
        return ''

def main():
    print("Welcome to Love Calculator")
    Your_Name = input("Please Provide Your Name: ")
    His_or_Her_Name = input("Please proivde His/Her Name: ")
    name = Your_Name + His_or_Her_Name
    print(name)
    result = love_calculator_logic(name)
    cond = message_condition(result)
    print(f"Your Love Score is {result}% {cond}")


if __name__ =="__main__":
    main()

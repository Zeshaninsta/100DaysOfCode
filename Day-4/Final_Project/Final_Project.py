# Game logic
def game_logic(user_choice):
    import random as rd
    ch = ["rock", "paper", "scissors"]
    computer = rd.choice(ch)
    user_choice = user_choice.lower()
    # user input validation
    if user_choice not in ch:
        return "Invalid choice. Please choose from rock, paper and scissors"
    if user_choice:
        print(f"computer chooses {computer}")
# game logic
    if user_choice == computer:
        return "check mate"
    elif user_choice == "rock" and computer == "scissors" or user_choice == "scissors" and computer == "paper" or user_choice == "paper" and computer == "rock":
        return "You win"
    else: 
        return "computer wins"
    return computer

# main function:wq
def main():
    user_choice = input("Which one do you choose? \n Rock \n Paper \n Scissors \n --------------------------------------------------------------------- \n")
    print("-------------------------------------------------------------------------")
    result = game_logic(user_choice)
    print(result)

if __name__=="__main__":
    main()

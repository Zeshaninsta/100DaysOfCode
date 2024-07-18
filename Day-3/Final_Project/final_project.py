def game_logic(direction):
    if direction == "left":
        decision = input("You come to lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: \n")
        if decision == "wait":
            door = input("You arrived at the island unharmed. There is a house with 3 doors, one red, one yellow and one blue. Which color do you choose? Blue, Yellow, Red: \n")
            if door == "yellow":
                return "You Found a treasure, You Win!"
            else:
                return "You Enterd a room of beast, Game Over"
        else:
            return "You Got attacked by an angry trout. Game Over"
    else:
        return "You fell into a Hole,Game Over"

def main():
    print('''

mmmmmmm mmmmm  mmmmmm   mm    mmmm  m    m mmmmm  mmmmmm
   #    #   "# #        ##   #"   " #    # #   "# #     
   #    #mmmm" #mmmmm  #  #  "#mmm  #    # #mmmm" #mmmmm
   #    #   "m #       #mm#      "# #    # #   "m #     
   #    #    " #mmmmm #    # "mmm#" "mmmm" #    " #mmmmm

   ''')
    print("welcome to treasure island")
    print("Your Mission is to find the treasure")
    direction = input("You're at a cross road. where do you want to go? left or right: \n")
    result = game_logic(direction)
    print(result)


if __name__ == "__main__":
    main()

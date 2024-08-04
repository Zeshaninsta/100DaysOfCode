def game_logic(board, user):
    row = int(user[0]) -1
    column = int(user[1]) -1
    board[column][row] = "X"
    return board

def main():
    row1 = ["😕","😕","😕"]
    row2 = ["😕","😕","😕"]
    row3 = ["😕","😕","😕"]
    board = [row1, row2, row3]
    for row in board:
        print(row)
    user = input("Where do you want to put the treasure? : ")
    game_logic(board, user)
    
    for row in board:
        print(row)
    
if __name__ == "__main__":
    main()

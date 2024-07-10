import numpy as np
from logo import logo_ttt

print(logo_ttt())

def print_board(array):
    print("-------------")
    for row in array:
        print("|", " | ".join(map(str, row)), "|")
        print("-------------")

def update_board(board,row,column,player):
    if 1 <= row <= 3 and 1 <= column <= 3:
        if board[row-1, column-1] == " ":
            board[row-1, column-1] = player
            player_flip=True
        else:
            print("Invalid move: Cell is already occupied.")
            player_flip=False
    else:
        print("Invalid input: Row and column must be between 1 and 3.")
        player_flip=False
    print_board(board)
    return player_flip

def check_win(board, player):
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    return " " not in board.flatten()

board = np.array([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])
print_board(board)
player1='X'
player2='0'
playing_player=1

while True:
    if playing_player % 2 == 0:
        player=player2
    else:
        player=player1
    print(F" => {player} Player Turn <=")
    board_row= int(input("Enter the Row Number(1,2,3): "))
    board_column= int(input("Enter the Column Number(1,2,3): "))
    player_flip=update_board(board,board_row,board_column,player)

    if player_flip:
        if check_win(board, player):
            print(f"Player {player} wins!")
            break
        elif check_draw(board):
            print("The game is a draw!")
            break
        playing_player += 1

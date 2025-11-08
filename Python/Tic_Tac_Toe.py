#generate a code to play tic tac toe game in python
import random
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def get_empty_positions(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
def tic_tac_toe():      
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        if current_player == "X":
            row, col = map(int, input("Enter your move (row and column 0-2): ").split())
        else:
            row, col = random.choice(get_empty_positions(board))
            print(f"Computer chose: {row} {col}")
        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        board[row][col] = current_player
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if not get_empty_positions(board):
            print_board(board)
            print("It's a tie!")
            break
        current_player = "O" if current_player == "X" else "X"
tic_tac_toe()

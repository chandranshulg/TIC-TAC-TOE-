#Chandranshu tic tac toe game 
print("Welcome to tic ta toe game by Chandranshu")

def print_board(board):
    """Function to print the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    """Function to check if the player has won."""
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def check_tie(board):
    """Function to check if the game is a tie."""
    return all([cell != " " for row in board for cell in row])

def tic_tac_toe():
    """Function to play the Tic Tac Toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter the row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter the column (0, 1, or 2): "))
        
        if board[row][col] == " ":
            board[row][col] = current_player
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif check_tie(board):
                print_board(board)
                print("The game is a tie!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("The cell is already occupied. Try again.")
    
    if input("Do you want to play again? (y/n): ").lower() == "y":
        tic_tac_toe()

tic_tac_toe()

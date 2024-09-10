# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if any player has won
def check_win(board, player):
    # Check rows, columns and diagonals for a win
    for row in board:
        if all(s == player for s in row):
            return True
    
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

# Function to check if the board is full (i.e., a draw)
def check_draw(board):
    return all(cell != " " for row in board for cell in row)

# Function to play the Tic-Tac-Toe game
def play_game():
    # Initialize an empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        print(f"Player {players[current_player]}'s turn.")

        # Get player's move
        try:
            row, col = map(int, input("Enter row and column (0, 1, 2) separated by a space: ").split())
        except ValueError:
            print("Invalid input. Please enter two numbers between 0 and 2.")
            continue

        # Validate move
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        # Place the player's move
        board[row][col] = players[current_player]

        # Check for win
        if check_win(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break

        # Check for draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch to the next player
        current_player = 1 - current_player

# Start the game
if __name__ == "__main__":
    play_game()
  

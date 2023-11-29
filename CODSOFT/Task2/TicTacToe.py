import random

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

# Function to get a list of available moves
def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

# Function for the AI to make a move
def ai_move(board):
    available_moves = get_available_moves(board)
    return random.choice(available_moves)

# Function to start the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = random.choice(players)

    print("Welcome to Tic Tac Toe! You are playing as", current_player)

    while True:
        print_board(board)

        if current_player == "X":  # Human's turn
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if board[row][col] == " ":
                board[row][col] = "X"
            else:
                print("That cell is already taken. Try again.")
                continue
        else:  # AI's turn
            move = ai_move(board)
            board[move[0]][move[1]] = "O"
            print("AI placed an 'O' at position:", move)

        if check_win(board, current_player):
            print_board(board)
            print(current_player, "wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the game
if __name__ == "__main__":
    play_game()
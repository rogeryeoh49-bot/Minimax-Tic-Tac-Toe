def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")


def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or \
            all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)


def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        print(f"Player {current_player}'s turn.")

        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter col (0, 1, 2): "))
        except ValueError:
            print("Invalid input. Please enter numbers 0, 1, or 2.")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Row and column must be between 0 and 2.")
            continue

        if board[row][col] != ' ':
            print("Cell already taken. Try again.")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


# Run the game
play_game()
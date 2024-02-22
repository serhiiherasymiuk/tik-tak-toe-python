def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False


def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))


def get_move(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (1, 2, 3): ")) - 1
            col = int(input(f"Player {player}, enter column (1, 2, 3): ")) - 1
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input! Row and column numbers must be between 1 and 3.")
                continue
            return row, col
        except ValueError:
            print("Invalid input! Please enter integers.")


def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row, col = get_move(current_player)

        if board[row][col] != ' ':
            print("That position is already taken. Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    play_game()

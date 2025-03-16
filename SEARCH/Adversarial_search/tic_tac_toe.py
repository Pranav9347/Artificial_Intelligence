import math

# Tic-Tac-Toe Board
board = [[' ' for _ in range(3)] for _ in range(3)]
scores = {"Player": 0, "System": 0, "Draw": 0}

# Scores for minimax
def evaluate(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != ' ':
            return 1 if board[row][0] == 'O' else -1
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return 1 if board[0][col] == 'O' else -1
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return 1 if board[0][0] == 'O' else -1
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return 1 if board[0][2] == 'O' else -1
    return 0

def is_moves_left(board):
    return any(board[i][j] == ' ' for i in range(3) for j in range(3))

def minimax(board, is_maximizing, alpha, beta):
    score = evaluate(board)
    if score == 1 or score == -1:
        return score
    if not is_moves_left(board):
        return 0
    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = max(best, minimax(board, False, alpha, beta))
                    board[i][j] = ' '
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = min(best, minimax(board, True, alpha, beta))
                    board[i][j] = ' '
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

def find_best_move():
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, False, -math.inf, math.inf)
                board[i][j] = ' '
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move

def print_board():
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner():
    score = evaluate(board)
    if score == 1:
        print("System wins!")
        scores["System"] += 1
        return True
    elif score == -1:
        print("You win!")
        scores["Player"] += 1
        return True
    elif not is_moves_left(board):
        print("It's a draw!")
        scores["Draw"] += 1
        return True
    return False

def play_game():
    global board
    while True:
        print_board()
        row, col = map(int, input("Enter your move (row and column): ").split())
        if board[row][col] != ' ':
            print("Invalid move! Try again.")
            continue
        board[row][col] = 'X'
        if check_winner():
            break
        print("System is making a move...")
        system_move = find_best_move()
        board[system_move[0]][system_move[1]] = 'O'
        if check_winner():
            break
    print_board()
    print(f"Scoreboard: Player {scores['Player']} - System {scores['System']} - Draws {scores['Draw']}")
    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again == 'y':
        board = [[' ' for _ in range(3)] for _ in range(3)]  # Reset board
        play_game()

play_game()
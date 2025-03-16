import math

def print_board(matrix):
    for row in matrix:
        print(" | ".join(row))
        print('-'*9)


def is_full(state):
    for row in state:
        for cell in row:
            if cell == ' ':
                return False
    return True


def is_win(state, player):
    # Row-test:
    if any(row == [player,player,player] for row in state):
        return True
    # Column-test:
    for j in range(3):
        if [player,player,player] == [state[i][j] for i in range(3)]:
            return True
    # Diagonals-test:
    if [state[0][0], state[1][1], state[2][2]] == [player] * 3 or [state[0][2], state[1][1], state[2][0]] == [player] * 3:
        return True



def minimax(state, is_maximizing):
    # Base cases:
    if is_win(state, 'X'): # Computer wins(1)
        return 1
    elif is_win(state, 'O'): # Human wins(-1)
        return -1
    elif is_full(state): # Draw case(0)
        return 0
    
    if is_maximizing: # max node
        utility = -math.inf
        for i in range(3):
            for j in range(3):
                if state[i][j] == ' ': # empty cell
                    state[i][j] = 'X'
                    utility = max(utility, minimax(state,False))
                    state[i][j] = ' '
    else: # min node
        utility = math.inf
        for i in range(3):
            for j in range(3):
                if state[i][j] == ' ': # empty cell
                    state[i][j] = 'O'
                    utility = min(utility, minimax(state,True))
                    state[i][j] = ' '
    return utility


def make_decision(state): # computer's turn(X):
    utility_val = -1
    # Find the next best move:
    for i in range(3):
        for j in range(3):
            if state[i][j] == ' ': # empty state
                state[i][j] = 'X'
                child_state_utility = minimax(state,False)
                state[i][j] = ' '
                if child_state_utility == 1:
                    state[i][j] = 'X'
                    print_board(state)
                    return
                if child_state_utility >= utility_val:
                    utility_val = child_state_utility
                    best_move = (i,j)
    i,j = best_move
    state[i][j] = 'X'
    print_board(state)
    return

# Main function:
# start_state = [[' ','O',' '],['X',' ',' '],[' ',' ',' ']] # X has already won here!
# print(minimax(start_state, True)) # minimax value is +1
start_state = [[' ' for _ in range(3)] for _ in range(3)]
print_board(start_state)
state = start_state
turn = "human"
while True:
    if is_win(state, 'X'):
        print("Computer Wins!")
        break
    elif is_win(state, 'O'):
        print("You Win!") # Which is never gonna happen
        break
    else:
        if is_full(state):
            print("Game is draw!")
            break
        if turn == "human":
            valid = False
            while not valid:
                i,j = map(int, input("Please enter row,column to place 'O'(0-2): ").split())
                if state[i][j] == ' ':
                    valid = True
                else:
                    print("Invalid cell!")
            state[i][j] = 'O'
            turn = "computer"
        elif turn == "computer":
            make_decision(state)
            turn = "human"

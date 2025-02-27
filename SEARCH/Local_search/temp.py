import random
import math

# Goal state
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Heuristic function: Manhattan Distance
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_row, goal_col = divmod(state[i][j] - 1, 3)
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance

# Generate all possible neighbors
def get_neighbors(state):
    neighbors = []
    empty_row, empty_col = find_empty_tile(state)
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    for move in moves:
        new_row, new_col = empty_row + move[0], empty_col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [row[:] for row in state]
            new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
            neighbors.append(new_state)

    return neighbors

# Find the position of the empty tile (0)
def find_empty_tile(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Hill Climbing with Random Restart
def iterative_hill_climbing(initial_state, iterations=15):
    current_state = initial_state
    for _ in range(iterations):
        if current_state == goal_state:
            return current_state  # Puzzle solved

        neighbors = get_neighbors(current_state)
        best_neighbor = min(neighbors, key=manhattan_distance)

        if manhattan_distance(best_neighbor) < manhattan_distance(current_state):
            current_state = best_neighbor
        else:
            # Random restart
            current_state = generate_random_state()

    return current_state  # Return the best state found

# Generate a random state
def generate_random_state():
    numbers = list(range(9))
    random.shuffle(numbers)
    return [numbers[i:i+3] for i in range(0, 9, 3)]

# Main
initial_state = [
    [3, 4, 8],
    [6, 0, 7],
    [5, 2, 1]
]

solution = iterative_hill_climbing(initial_state, iterations=15)
print("Final State:")
for row in solution:
    print(row)
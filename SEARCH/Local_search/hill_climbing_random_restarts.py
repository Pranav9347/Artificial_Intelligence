import random
import copy

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def generate_random_state():
    numbers = list(range(9))
    random.shuffle(numbers)
    return [numbers[:3], numbers[3:6], numbers[6:]]

def find_blank_tile(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    i0, j0 = find_blank_tile(state)
    neighbors = []
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for di, dj in moves:
        new_i, new_j = i0 + di, j0 + dj
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = copy.deepcopy(state)
            new_state[i0][j0], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i0][j0]
            neighbors.append(new_state)
    return neighbors

def heuristic(state):
    misplaced = sum(state[i][j] != goal_state[i][j] for i in range(3) for j in range(3))
    return misplaced

def hill_climbing(start_state):
    current_state = start_state
    while True:
        neighbors = get_neighbors(current_state)
        best_neighbor = min(neighbors, key=heuristic, default=current_state)
        if heuristic(best_neighbor) >= heuristic(current_state):
            return current_state  # Local optimum reached
        current_state = best_neighbor

def iterative_hill_climbing(iterations=15):
    for i in range(iterations):
        start_state = generate_random_state()
        print(f"Iteration {i+1}: Starting state:")
        for row in start_state:
            print(row)
        result = hill_climbing(start_state)
        print("Final state:")
        for row in result:
            print(row)
        print("Misplaced tiles:", heuristic(result))
        print("-------------------")
        if result == goal_state:
            print("Solution found!")
            return result
    print("No optimal solution found within iterations.")
    return None

if __name__ == "__main__":
    iterative_hill_climbing()

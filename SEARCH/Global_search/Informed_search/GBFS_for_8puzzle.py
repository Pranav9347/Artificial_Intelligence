# GBFS algorithm to solve the 8-puzzle game

import heapq

def MoveGen(state):
    """Generates all possible moves from the given state."""
    neighbors = []
    zero_index = state.index(0)  # Find the blank space

    # Possible moves based on the blank space position
    moves = {
        0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
        3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
        6: [3, 7], 7: [4, 6, 8], 8: [5, 7]
    }

    for move in moves[zero_index]:
        new_state = list(state)
        new_state[zero_index], new_state[move] = new_state[move], new_state[zero_index]
        neighbors.append(tuple(new_state))  # Store states as tuples

    return neighbors

def GBFS(start, goal, h):
    count = 0
    open_list = [(h(start), start)]
    closed = set()  # Visited states
    parent = {start: None}

    while open_list:
        count += 1
        _, current = heapq.heappop(open_list)
        
        if current in closed:
            continue  # Skip if already visited

        print("Expanding:", current)
        closed.add(current)

        if current == goal:
            print("Goal reached!")
            print("Number of moves: ",count)
            return parent

        for neighbor in MoveGen(current):
            if neighbor not in closed:
                parent[neighbor] = current
                heapq.heappush(open_list, (h(neighbor), neighbor))

    return None  # No solution found

# Example heuristic: Number of misplaced tiles
def heuristic(state):
    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    return sum(1 for i in range(9) if state[i] != goal_state[i] and state[i] != 0)

# Initial state
start_state = (3,4,8,6,0,7,5,2,1)
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0) # takes 285 frickin moves to solve this: not optimal!

GBFS(start_state, goal_state, heuristic)

import copy

# I = [
#         [3,4,8],
#         [6,0,7],
#         [5,2,1]
#     ]
    
I = [
        [1,2,3],
        [4,0,6],
        [7,5,8]
    ] # try this I: it reaches goal!
# G = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,0]
# ]
goal_sequence = [I]

def MoveGen(S):
    # determine the number of possible moves(neighbors) from current state
    # determine position of 0
    neighbors = []
    i0 = -1
    j0 = -1
    for i in range(len(S)):
        for j in range(len(S)):
            if(S[i][j] == 0):
                i0 = i
                j0 = j

    new_neighbor = copy.deepcopy(S)
    if (i0-1)>=0: # top swap
        new_neighbor[i0][j0], new_neighbor[i0-1][1] = new_neighbor[i0-1][1], new_neighbor[i0][j0]
        neighbors.append(new_neighbor)
        new_neighbor = copy.deepcopy(S)
    if (j0-1)>=0: # left swap
        new_neighbor[i0][j0], new_neighbor[i0][j0-1] = new_neighbor[i0][j0-1], new_neighbor[i0][j0]
        neighbors.append(new_neighbor)
        new_neighbor = copy.deepcopy(S)
    if (j0+1)<=(len(S)-1): # bottom swap
        new_neighbor[i0][j0], new_neighbor[i0][j0+1] = new_neighbor[i0][j0+1], new_neighbor[i0][j0]
        neighbors.append(new_neighbor)
        new_neighbor = copy.deepcopy(S)
    if(i0+1)<=(len(S)-1): # right swap
        new_neighbor[i0][j0], new_neighbor[i0+1][1] = new_neighbor[i0+1][1], new_neighbor[i0][j0]
        neighbors.append(new_neighbor)
        new_neighbor = copy.deepcopy(S)
    return neighbors



def Heuristic(S):
    mismatch = 0
    for i in range(len(S)):
        for j in range(len(S)):
            if i==2 and j==2:
                if S[i][j] != 0:
                    mismatch += 1
            elif S[i][j] != 3*i+j+1:
                mismatch += 1
    return mismatch
    
    
def Best_neighbor(configs):
    state_hVal_pair = {}
    for state in configs:
        state_tuple = tuple(tuple(row) for row in state)
        state_hVal_pair[state_tuple] = Heuristic(state)
    next_best_tuple = min(state_hVal_pair,key=state_hVal_pair.get)
    next_best = [list(row) for row in next_best_tuple]
    return next_best


def Hill_Climbing(S):
    global goal_sequence
    print("Heuristic: ", Heuristic(S))
    current_state = S
    best = Heuristic(current_state)
    if best == 0: # base-case for recursion
        return goal_sequence
    neighbors = MoveGen(current_state)
    next_best_state = Best_neighbor(neighbors)
    if Heuristic(next_best_state) >= best: # Local minima case
        print("Stuck in local minima!")
        print("Heuristic: ", Heuristic(next_best_state))
        return []
    goal_sequence.append(next_best_state)
    return Hill_Climbing(next_best_state)
    

# print(Heuristic(G))
Hill_Climbing(I)

for state in goal_sequence:
    for i in range(len(state)):
        for j in range(len(state)):
            print(state[i][j], end = " ")
        print("")
    print("Next: ")
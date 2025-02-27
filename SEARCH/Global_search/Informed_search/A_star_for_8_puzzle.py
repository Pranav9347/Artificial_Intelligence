import copy
import heapq
inf = float('inf')

# I = [
#         [2,8,3],
#         [1,6,4],
#         [7,0,5]
#     ]

# G = [
#     [1,2,3],
#     [8,0,4],
#     [7,6,5]
# ]

I = [
    [3, 4, 8],
    [6, 0, 7],
    [5, 2, 1]
]
G = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
goal_sequence = []

def MoveGen(S):
    # determine the number of possible moves(neighbors) from current state
    # determine position of 0
    neighbors = []
    i0 = -1
    j0 = -1
    for i in range(3):
        for j in range(3):
            if(S[i][j] == 0):
                i0 = i
                j0 = j

    new_neighbor = copy.deepcopy(S)
    if (i0-1)>=0: # top swap
        new_neighbor[i0][j0], new_neighbor[i0-1][j0] = new_neighbor[i0-1][j0], new_neighbor[i0][j0]
        neighbors.append(new_neighbor)
        new_neighbor = copy.deepcopy(S)
    if (j0-1)>=0: # left swap
        new_neighbor[i0][j0], new_neighbor[i0][j0-1] = new_neighbor[i0][j0-1], new_neighbor[i0][j0]
        neighbors.append(new_neighbor)
        new_neighbor = copy.deepcopy(S)
    if (j0+1)<=2: # bottom swap
        new_neighbor[i0][j0], new_neighbor[i0][j0+1] = new_neighbor[i0][j0+1], new_neighbor[i0][j0]
        neighbors.append(new_neighbor)
        new_neighbor = copy.deepcopy(S)
    if(i0+1)<=2: # right swap
        new_neighbor[i0][j0], new_neighbor[i0+1][j0] = new_neighbor[i0+1][j0], new_neighbor[i0][j0]
        neighbors.append(new_neighbor)
        new_neighbor = copy.deepcopy(S)
    return neighbors



def h(S):
    mismatch = 0
    for i in range(3):
        for j in range(3):
            if S[i][j] != G[i][j]:
                mismatch += 1
    return mismatch



def A_star(S): # S is a matrix
    global goal_sequence
    best_cost = inf
    min_heap = [(h(S),0,h(S),S,[])] # NodeTriplet:(g(n),n,path_to_n)
    while min_heap:
        f, g, heuristic, curr, path = heapq.heappop(min_heap)
        path.append(curr)
        if heuristic == 0: # goal_test(S) is passed then
            if g < best_cost:
                best_cost = g
                best_path = path
                print("Minimum number of moves = ", best_cost)
                # print("Best sequence of moves = ", best_path)
                goal_sequence = best_path
                return
        else:
            if g > best_cost: # then prune that subtree
                continue
            else:
                neighbors = MoveGen(curr)
                for child in neighbors:
                    if child not in path:
                        new_g = g+1 # increment the number of moves for the child node
                        heapq.heappush(min_heap, (new_g+h(child), new_g, h(child), child, path.copy()))
    return

# print(Heuristic(G))
A_star(I)


print("Move Sequence: ")
for state in goal_sequence:
    for i in range(len(state)):
        for j in range(len(state)):
            print(state[i][j], end = " ")
        print("")
    print('  \u2193')  # ↓ (downward arrow)
print("GOAL!")
import heapq
inf = float('inf')

# n = 7
# src = 0
# graph = [
#             [0,6,3,inf,inf,inf,inf],
#             [6,0,inf,2,inf,inf,inf],
#             [3,inf,0,4,7,inf,inf],
#             [inf,2,4,0,1,5,inf],
#             [inf,inf,7,1,0,2,inf],
#             [inf,inf,inf,5,2,0,3],
#             [inf,inf,inf,inf,inf,3,0]
#     ]
# GOAL = 6

# # Define the heuristic values for each node
# h = [8,6,5,3,2,1,0]

n = 23
src = 8
graph = [
    [0,inf,inf,inf,23,inf,inf,22,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf],
    [inf,0,13,inf,33,inf,inf,inf,37,inf,35,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf],
    [inf,13,0,23,inf,24,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf],
    [inf,inf,23,0,inf,inf,33,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf],
    [23,33,inf,inf,0,inf,inf,inf,29,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf],
    [inf,inf,24,inf,inf,0,inf,inf,inf,inf,22,inf,21,64,inf,inf,inf,inf,inf,inf,inf,inf,inf],
    [inf,inf,inf,33,inf,inf,0,inf,inf,inf,inf,inf,inf,33,inf,inf,inf,inf,inf,inf,inf,inf,inf],
    [22,inf,inf,inf,inf,inf,inf,0,22,inf,inf,inf,inf,inf,23,inf,inf,inf,inf,inf,inf,inf,inf],
    [inf,37,inf,inf,29,inf,inf,22,0,12,inf,22,inf,inf,inf,21,inf,inf,inf,inf,inf,inf,inf],
    [inf,inf,inf,inf,inf,inf,inf,inf,12,0,12,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf],
    [inf,35,inf,inf,inf,22,inf,inf,inf,12,0,inf,21,inf,inf,inf,33,inf,inf,inf,inf,inf,inf],
    [inf,inf,inf,inf,inf,inf,inf,inf,22,inf,inf,0,inf,inf,23,21,inf,inf,inf,inf,inf,inf,inf],
    [inf,inf,inf,inf,inf,21,inf,inf,inf,inf,21,inf,0,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf],
    [inf,inf,inf,inf,inf,64,33,inf,inf,inf,inf,inf,inf,0,inf,inf,inf,21,inf,inf,inf,inf,43],
    [inf,inf,inf,inf,inf,inf,inf,23,inf,inf,inf,23,inf,inf,0,22,inf,inf,21,inf,inf,inf,inf],
    [inf,inf,inf,inf,inf,inf,inf,inf,21,inf,inf,21,inf,inf,22,0,12,inf,inf,inf,inf,inf,inf],
    [inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,33,inf,inf,inf,inf,12,0,inf,inf,inf,inf,inf,inf],
    [inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,21,inf,inf,inf,0,inf,32,inf,inf,44],
    [inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,21,inf,inf,inf,0,inf,21,inf,inf],
    [inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,32,inf,0,35,33,inf],
    [inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,21,35,0,41,inf],
    [inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,33,41,0,22],
    [inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,43,inf,inf,inf,44,inf,inf,22,0]
]
GOAL = 22
# Define the heuristic values for each node
h = [140,110,100,80,120,80,50,120,100,90,80,100,60,40,100,80,70,40,80,50,60,20,0]

def MoveGen(node):
    neighbors = []
    for i in range(n):
        if graph[node][i] != inf:
            neighbors.append(i)
    return neighbors


def A_star():
    best_cost = inf
    min_heap = [(h[0],0,h[0],src,[])] # NodeTriplet:(g(n),n,path_to_n)
    while min_heap:
        f, g, heuristic, curr, path = heapq.heappop(min_heap)
        path.append(curr)
        if curr == GOAL:
            if g < best_cost:
                best_cost = g
                best_path = path
                print("best_cost = ", best_cost)
                print("best_path = ", best_path)
        else:
            if g > best_cost: # then prune that subtree
                continue
            else:
                neighbors = MoveGen(curr)
                for child in neighbors:
                    if child not in path:
                        new_g = g+graph[curr][child]
                        heapq.heappush(min_heap, (new_g+h[child], new_g, h[child], child, path.copy()))
    return

A_star()


'''
A* search finds the shortest path to goal by expanding nodes based on f(n)=g(n)+h(n): (path cost from src to n) + (estimated cost to goal). If a path cost > best tentative cost, then that subtree is pruned like B&B.

- A* is a combination of B&B and GBFS. It solves the limitations of both:
g(n): ensures shortest path from src to goal which GBFS won't
h(n): ensures direction is goal oriented- doesn't explore shorter paths which are irrelevant to goal, which B&B would.

- By combining them, g(n) pulls the search agent to the source(to ensure spath) and h(n) pushes the agent towards the goal(for efficiency). 

    For this, h(n) needs to be a good estimate:
** Admissable properties of A*:
- h(n) should not be an overestimate(but should be an underestimate): h(n)<=h*(n)
- Edge cost should be positive

Complexity:
Time: O(b^d log(b^d)) in worst case: h(n) is a bad estimate
Space: O(b^d)

'''
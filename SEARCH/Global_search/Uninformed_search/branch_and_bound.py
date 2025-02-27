import heapq
inf = float('inf')

# graph = [
#     [0,2,inf,5,inf],
#     [2,0,5,1,inf],
#     [inf,5,0,inf,3],
#     [5,1,inf,0,10],
#     [inf,inf,3,10,0]
# ]
# src = 0
# n = 5
# GOAL = 4
n=8
src=0
graph = [      [0,4,10,inf,inf,inf,inf,5],
                    [4,0,11,15,inf,inf,inf,inf],
                    [10,11,0,13,3,inf,inf,11],
                    [inf,15,13,0,6,5,inf,inf],
                    [inf,inf,3,6,0,2,5,inf],
                    [inf,inf,inf,5,2,0,8,inf],
                    [inf,inf,inf,inf,5,8,0,7],
                    [5,inf,11,inf,inf,inf,7,0]
                ]
GOAL = 5


def MoveGen(node):
    neighbors = []
    for i in range(n):
        if graph[node][i] != inf:
            neighbors.append(i)
    return neighbors


def B_and_B():
    best_cost = inf
    min_heap = [(0,0,[])] # NodeTriplet:(g(n),n,path_to_n)
    while min_heap:
        g, n, path = heapq.heappop(min_heap)
        path.append(n)
        if n == GOAL:
            if g < best_cost:
                best_cost = g
                best_path = path
                print("best_cost = ", best_cost)
                print("best_path = ", best_path)
        else:
            if g > best_cost: # then prune that subtree
                continue
            else:
                neighbors = MoveGen(n)
                for child in neighbors:
                    if child not in path:
                        heapq.heappush(min_heap, (g+graph[n][child], child, path.copy()))
    return

B_and_B()


'''
Branch and Bound finds the shortest path to goal by expanding nodes based on g(n): path cost from src to n (Branching). If a path cost > best tentative cost, then that subtree is pruned (Bound). 

- B&B is basically best-first-search(GBFS) with g(n) as priority along with pruning. And both BGFS and B&B are derivatives of BFS, as they use priority queue instead of queue
- The path that B&B constructs is purely based on the g(n) and hence is the shortest path to goal
- If goal does not occur in shorter paths, it'll have to explore all paths and in worst case it performs like BFS: Limitation of B&B

Complexity:
Time: O(b^d log(b^d)) in worst case: goal occurs in longest path from src
Space: O(b^d)

'''
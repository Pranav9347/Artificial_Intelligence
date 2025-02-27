import heapq
inf = float('inf')

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
                ] #spath=49
# GOAL = 5

# n=4
# src=0
# graph=[
#     [0,20,10,12],
#     [20,0,15,11],
#     [10,15,0,17],
#     [12,11,17,0]
# ] #spath=48


def MoveGen(node):
    neighbors = []
    for i in range(n):
        if graph[node][i] != inf and node != i:
            neighbors.append(i)
    return neighbors

def all_in_path(path):
    for i in range(n):
        if i not in path:
            return False
    return True


def B_and_B():
    best_cost = inf
    min_heap = [(0,src,[])] # NodeTriplet:(g(n),n,path_to_n)
    while min_heap:
        g, n, path = heapq.heappop(min_heap)
        path.append(n)
        if n == src and all_in_path(path):
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
                    if child == src or child not in path:
                        heapq.heappush(min_heap, (g+graph[n][child], child, path.copy()))
    return

B_and_B()


'''
Branch and Bound finds the shortest path to goal by expanding nodes based on g(n): path cost from src to n (Branching). If a path cost > best tentative cost, then that subtree is pruned (Bound). 

- B&B is basically best-first-search(GBFS) with g(n) as priority along with pruning. And both BGFS and B&B are derivatives of BFS, as they use priority queue instead of queue

Complexity:
Time: O(b^d log(b^d)) in worst case, but usually it's less than that
Space: O(b^d)

'''
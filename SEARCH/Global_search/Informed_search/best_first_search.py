import heapq

inf = float('inf')
src = 0
n = 7
GOAL = 6
graph = [
            [0,6,3,inf,inf,inf,inf],
            [6,0,inf,2,inf,inf,inf],
            [3,inf,0,4,7,inf,inf],
            [inf,2,4,0,1,5,inf],
            [inf,inf,7,1,0,2,inf],
            [inf,inf,inf,5,2,0,3],
            [inf,inf,inf,inf,inf,3,0]
    ]
h = [8,6,5,3,2,1,0] # heuristic values

def reconstruct_path(parent):
    i = GOAL
    stack = []
    while i != -1:
        stack.append(i)
        top = stack[-1]
        i = parent[top]
    print("Path to goal:", "->".join(map(str, stack[::-1])))  #reverse stack

def MoveGen(state):
    next_moves = []
    for i in range(n):
        if graph[state][i] != inf:
            next_moves.append(i)
    return next_moves


def GBFS():
    parent = [-1]*n
    closed = [False]*n
    open = [(h[src],src)] # open here is a min_heap
    open_set = {src}  # Track nodes in the heap to avoid duplicates
    curr = src

    while open:
        heuristic, curr = heapq.heappop(open)
        open_set.remove(curr)  # Remove from tracking set
        print("Node with min h(n): ",curr)
        closed[curr] = True
        if curr == GOAL:
            return parent
        else:
            neighbors = MoveGen(curr)
            for neighbor in neighbors:
                if not closed[neighbor]:
                    if neighbor not in open_set:
                        parent[neighbor] = curr
                        heapq.heappush(open,(h[neighbor],neighbor))
                        open_set.add(neighbor)
    return []

path_to_goal = GBFS()
reconstruct_path(path_to_goal) # may not be shortest

'''
Greedy Best-First-Search: GBFS

Similar in structure to BFS but uses priority queue instead of a normal queue. GBFS has an additional information of the heuristic(estimate to the goal from the current state) which becomes the priority.

Using the heuristic it tries exploring the graph not level-by-level but, by the path guided by the heuristic estimate. If the heristic is a good estimate, it can significantly prune the search space.

The path that GBFS constructs is purely based on the h(n) and hence need not be the shortest path to goal: Limitation of GBFS

If h(n) is not a good estimate then GBFS is basically BFS. So in worst case, GBFS is same as BFS.
Complexity:
Average case depends on h(n)
Time: O(b^d)..worst case-h(n) is a bad estimate
Space: O(b^d log(b^d))..worst case
'''
import math
NO_EDGE = math.inf

GOAL = 5

n = 6 # number of states
graph = [
    [0,1,NO_EDGE,NO_EDGE,NO_EDGE,NO_EDGE],
    [1,0,1,NO_EDGE,1,NO_EDGE],
    [NO_EDGE,1,0,1,1,NO_EDGE],
    [NO_EDGE,NO_EDGE,1,0,NO_EDGE,NO_EDGE],
    [NO_EDGE,1,1,NO_EDGE,0,1],
    [NO_EDGE,NO_EDGE,NO_EDGE,NO_EDGE,1,0]
]


def reconstruct_path(parent):
    i = GOAL
    stack = []
    while i != -1:
        stack.append(i)
        top = stack[-1]
        i = parent[top]
    while stack:
        print(stack.pop(), end='->')
    # print("Shortest path to goal:", "->".join(map(str, stack[::-1])))  # Or use this: reverse stack

visited = [False]*n
parent = [-1]*n
def DLS(src, d): # Depth-limited-search
    global visited
    global parent
    visited[src] = True
    if d == 0:
        if src == GOAL:
            return parent
        else:
            return []
    for i in range(n):
        if graph[src][i] != NO_EDGE and not visited[i]:
            parent[i] = src
            ret = DLS(i,d-1)
            if len(ret)>0: # GOAL found
                return ret # path to goal: Parent
    for i in range(n): # no adjacent unvisited neighbor exists, so while backtracking mark its children as unvisted
        if parent[i] == src:
            visited[i] = False
    return [] # goal not found


def DFID(start, max_depth):
    global visited
    global parent
    for depth in range(max_depth+1):
        visited = [False]*n
        parent = [-1]*n
        ret = DLS(start, depth)
        if len(ret) > 0:
            print("Goal found at depth: ", depth)
            reconstruct_path(ret)
    return


DFID(0, 3) # max_depth=3

'''
DEPTH-FIRST-ITERATIVE-DEEPENING:
Perform Depth limited Searches recursively with increasing depth bounds. At iteration d, (DLS(d)), all paths which are of length d from the source are explored.

- Combines the completeness of BFS with space efficiency of DFS.
- Guarentees solution even with infinitely deep or broad graphs
- Guarentees shortest path in unweighted graphs
Complexity analysis:
Space: O(d), d = depth
Time: O(b^d), b= branching factor
'''
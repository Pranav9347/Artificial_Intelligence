import math
NaN = math.inf # represents no edge

GOAL = 5

n = 6 # number of states
adj_matrix = [
    [0,1,NaN,NaN,NaN,NaN],
    [1,0,1,NaN,1,NaN],
    [NaN,1,0,1,1,NaN],
    [NaN,NaN,1,0,NaN,NaN],
    [NaN,1,1,NaN,0,1],
    [NaN,NaN,NaN,NaN,1,0]
]

def DFS_goal_search(state_space, init_state):
    n = len(state_space)
    stack = []
    parent = [-1]*n
    closed = [False]*n
    stack.append(init_state)
    closed[init_state] = True # mark as visited
    while stack:
        top = stack[-1]
        for i in range(n): # if adjacent unvisited neighbor exists
            if state_space[top][i] != NaN and not closed[i]:
                parent[i] = top
                closed[i] = True
                if i == GOAL:
                    print("closed: ", closed)
                    print("parent: ", parent)
                    return parent
                else:
                    stack.append(i)
                    break
        if stack[-1] == top: # no unvisited neighbor exists
            stack.pop()
    return parent

def reconstruct_path(parent):
    i = GOAL
    stack = []
    while i != -1:
        stack.append(i)
        top = stack[-1]
        i = parent[top]
    while stack:
        print(stack.pop(), end='->')

parent = DFS_goal_search(adj_matrix, 0)
print("Path to goal: ",end="")
reconstruct_path(parent)

'''
DEPTH-FIRST-SEACRH:

Computational complexity:
Space: O(d), d = depth
Time: O(b^d), b = branching factor

Search by DFS will not satisfy completeness if depth is infinite
Search by DFS will not ensure shortest path
Better than BFS in terms of space complexity
'''
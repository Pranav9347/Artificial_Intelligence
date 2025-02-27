import math
NaN = math.inf # represents no edge

from queue import Queue
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

def BFS_goal_search(state_space, init_state):
    n = len(state_space)
    q = Queue()
    parent = [-1]*n
    spath = [-1]*n
    closed = [False]*n
    q.put(init_state)
    spath[init_state] = 0
    closed[init_state] = True # mark as visited
    while not q.empty():
        front = q.get()
        for i in range(n): # enqueue all unvisited neighbors of front
            if state_space[front][i] != NaN and not closed[i]:
                closed[i] = True
                parent[i] = front
                spath[i] = spath[front]+1
                if i == GOAL:
                    print("visited: ",closed)
                    print("spath: ", spath)
                    print("parent: ", parent)
                    return parent
                else:
                    q.put(i)
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
    # print("Shortest path to goal:", "->".join(map(str, stack[::-1])))  # Or use this: reverse stack

parent = BFS_goal_search(adj_matrix, 0)
print("Shortest path to goal: ",end="")
reconstruct_path(parent)

'''
BREADTH-FIRST-SEARCH:

Computational complexity:
Space: O(b^d), d = depth, b = branching factor
Time: O(b^d)

Search by BFS satisfies completeness
Search by BFS ensures shortest path for unweighted graphs only.
'''
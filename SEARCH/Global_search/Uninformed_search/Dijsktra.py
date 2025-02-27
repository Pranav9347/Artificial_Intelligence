import heapq

inf = float('inf')
src = 0
# n = 5 # number of vertices
# GOAL = 4
# graph = [
#             [0,12,10,19,8],
#             [12,0,3,7,6],
#             [10,3,0,2,20],
#             [19,7,2,0,4],
#             [8,6,20,4,0]
#         ]

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


def reconstruct_path(parent):
    i = GOAL
    stack = []
    while i != -1:
        stack.append(i)
        top = stack[-1]
        i = parent[top]
    while stack:
        print(stack.pop(), end='->')


def Dijktra():
    spaths = [inf]*n # initially mark all nodes at inf distance from src
    parent = [-1]*n
    visited = [False]*n
    spaths[src] = 0
    min_heap = [(0,src)] # initialize min-heap with src (spath,src_index)

    while min_heap:
        dist, v = heapq.heappop(min_heap) # extract next vertex with min dist from src
        if visited[v]:
             continue

        visited[v] = True
        for i in range(n):
            if  graph[v][i] != inf and not visited[i]: #if v's neighbor is unvisited
                new_dist = spaths[v] + graph[v][i]
                if new_dist < spaths[i]: # Relax the edge(v,i)
                    spaths[i] = new_dist
                    parent[i] = v
                    heapq.heappush(min_heap,(spaths[i],i))
    
    return spaths, parent


spaths, parent = Dijktra()
for i in range(len(spaths)):
    print(f"Shortest path length from src to vertex {i}: {spaths[i]}")

print("Path to goal: ",end="")
reconstruct_path(parent)

'''
- Finds shortest path from source vertex to all other vertices
- Works for weighted graphs as well as unweighted graphs
- Requires the entire state space beforehand

Algorithm:
Starting from source node, visit all nodes, in the order of the tentative shortest paths(greediness). This greediness(extract min) can be implemented efficiently using min heap
While visiting a node v, relax all edges (v,i) for all unvisited verices i
Relax(u,v): if new_dist=dist[u]+graph[u][v]<d[v], then update d[v] to new_dist

Computational complexity:
Space: O(n^2)
Time: O(n^2 logn)
'''
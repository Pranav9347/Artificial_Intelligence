Global search is a goal state search problem which explores the state space systematically and in a global fashion:
- Always guarentee a solution if one exists, because it considers the global perspective and hence backtracking if stuck in local optima.
- Usually are more memory and time intensive because of their exhaustive search.
- Is of two types: Uninformed/Blind search and Informed/heuristic algorithms

- Uninformed search algorithms: Search the state space for goal without any knowledge about the goal or its direction. Hence are more inefficient compared to Informed searches
1. DFS
2. Dijkstra's: (only Dijktstra's requires the entire state space/graph beforehand)
3. BFS
4. DFID
5. B&B: g(n) which is the actual path cost from src to n

- Informed search or Heuristic algorithms: Use the knowledge of estimated cost to the goal from every node: h(n) and efficiently try to move in the direction of the goal
1. GBFS: h(n) only: estimated cost from n to goal
2. A*: h(n) + g(n): combines the power of B&B and GBFS. Always finds the optimal path to goal and efficiently provided h(n) is admissible.
h(n) pushes the agent towards the goal and g(n) pulls it towards the source to ensure optimal path in an efficient search

Advantages:
- Completeness: Always guarantee a solution if 1 exists
- Best suited for small search spaces 
- Used if solution finding is important than efficiemcy

Disadvantages:
- Memory and time intensive compared to local search algorithms
- Large state spaces make them very slow

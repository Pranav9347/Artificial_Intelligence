Local search problems differ from global search in the sense that each state can be a potential solution. The objective of local search is to find the most optimal solution(global optima) state. Whereas global search problems fundamentally handle problems with a unique goal state, local search finds the best suitable state.

Better is a local search algorithm if it returns a solution close to the global optimum.

Local search is an optimization problem (whose objective is to find the optimal solution):
- Incrementally moves to a better solution from the current state till no further improvements are possible(local optima).
- Does not always guarentee a solution(global optima) even if one exists, because it considers the local perspective(possibility of getting stuck in local optima),  though better local searches  try to overcome this problem.
- Usually take less memory and time because of their local search.
- Can be considered as informed searches as the measure of how good a state is based on the heurisitc value(estimated cost from the goal)

    Using local search to solve goal-state search problems in AI:
- In case of goal state search in a state space, each state can be thought of as a heuristic function(h_value):
Goal of the search is to optimize(minimize) the heuristic function: search for the state with optimal(min) h_value. The most optimal h_value will be the goal:
Start state has the highest h_value. The local search progressively chooses state which improves the h_value at each step. Finally, hoping to end up at the goal.

- This approach has a major drawback. If from a paricular state, no further improvements seem to be possible then it gets stuck in local optima and considers it as goal. But the real goal is the global optima. There are several approaches which could potentially solve this:
* ignore the previous few visited states and backtrack to escape local optima: Tabu search
*  involve random restarts to randomly choose the start state whenever it gets stuck in local optima: Random-restart hill climbing
* Stochastic approaches which give a probability of a good move and a bad move: Simulated annealing

These random restarts will disrupt the path to goal and hence only the goal can be found and not the path to it

1. Hill Climbing algorithm
2. Tabu Search, Beam Search
3. Hill climbing with random restarts
4. Simulated annealing
5. Genetic algorithm


Advantages:
- Memory and time efficient compared to global search algorithms
- Best suited for large search spaces where efficiency is important

Disadvantages:
- No completeness: Does not always guarantee a solution even if 1 exists

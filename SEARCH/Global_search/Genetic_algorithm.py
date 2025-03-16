# Solving Traveling Salesman problem(TSP) using genetic algorithm(GA)

import random
import math

Population = []
Population_size = 4
generations = 30
sample = [1,2,3,4]

src = 0
graph = [
            [0,12,10,19,8],
            [12,0,3,7,6],
            [10,3,0,2,20],
            [19,7,2,0,4],
            [8,6,20,4,0]
        ]



def generate_population():
    global Population
    for i in range(Population_size):
        candidate = sample[:]
        random.shuffle(candidate)
        Population.append(candidate)


def fitness(route):
    total_cost = 0
    prev = src
    for city in route:
        total_cost += graph[prev][city]
        prev = city
    total_cost += graph[city][src]
    return total_cost


def crossover(parents):
    parent1, parent2 = parents
    offspring = []
    crossover_point = math.floor(random.random()*4)
    offspring = parent1[:crossover_point]
    # offspring.extend(parent2[crossover_point:]): this will add duplicates
     # Second part: take values from parent2 that aren't already in offspring
    for item in parent2[crossover_point:]:
        if item not in offspring:
            offspring.append(item)
    for item in parent1:
        if item not in offspring:
            offspring.append(item)
    return offspring
    

def mutation(chromosome):
    positions = [1, 2, 3, 0]
    pos1, pos2 = random.sample(positions.copy(), 2)
    chromosome[pos1],chromosome[pos2] = chromosome[pos2],chromosome[pos1]
    return chromosome
    


def Genetic_Algorithm():
    global Population
    generate_population()
    
    for generation in range(generations):
        print("Generation :", generation+1)
        # Selection:
        route_cost_tuple = []
        for route in Population:
            cost = fitness(route)
            route_cost_tuple.append((cost, route))
        
        route_cost_tuple = sorted(route_cost_tuple, key=lambda x:x[0])
        print("Initial Population: ", route_cost_tuple)
        selected = route_cost_tuple[:2]
        print("Selected best routes:", selected)
        # Crossover:
        temp = [x[1] for x in selected]
        selected = temp
        offspring = crossover(selected)
        # Mutation:
        mutated_offspring = mutation(offspring)
        Population.clear()
        Population = selected[:]
        Population.append(offspring)
        Population.append(mutated_offspring)
    return selected[0]
    
    
best_route = Genetic_Algorithm()
print(f"cost = {fitness(best_route)}, Best route:")
optimal_route = [0]
optimal_route.extend(best_route)
optimal_route.append(0)
print(optimal_route)


#Implementation of Simple genetic algorithm
import random

# Fitness function
def fitness(x):
    return x * x

# Convert binary to decimal
def binary_to_decimal(binary):
    return int(binary, 2)

# Initial population
population = ['10101', '11100', '01010', '00111']
print("Initial Population:", population)

# Evaluate fitness
fitness_values = []
for chrom in population:
    x = binary_to_decimal(chrom)
    fitness_values.append(fitness(x))

print("Fitness Values:", fitness_values)

# Selection (best two)
sorted_pop = [x for _, x in sorted(zip(fitness_values, population), reverse=True)]
parent1, parent2 = sorted_pop[0], sorted_pop[1]
print("Selected Parents:", parent1, parent2)

# Crossover (single point)
point = 2
child1 = parent1[:point] + parent2[point:]
child2 = parent2[:point] + parent1[point:]
print("After Crossover:", child1, child2)

# Mutation (flip one bit)
def mutation(child):
    index = random.randint(0, len(child)-1)
    mutated = list(child)
    mutated[index] = '1' if child[index] == '0' else '0'
    return ''.join(mutated)

child1 = mutation(child1)
child2 = mutation(child2)

print("After Mutation:", child1, child2)

# New population
new_population = [parent1, parent2, child1, child2]
print("New Population:", new_population)

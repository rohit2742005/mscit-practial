#Create two classes: City and Fitness using Genetic algorithm
import random
import math
import matplotlib.pyplot as plt

# ---------------- CITY CLASS ----------------
class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, city):
        return math.sqrt((self.x - city.x)**2 + (self.y - city.y)**2)


# ---------------- FITNESS CLASS ----------------
class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = self.calculate_distance()
        self.fitness = 1 / self.distance

    def calculate_distance(self):
        total = 0
        for i in range(len(self.route)):
            from_city = self.route[i]
            to_city = self.route[(i + 1) % len(self.route)]
            total += from_city.distance(to_city)
        return total


# ---------------- GA FUNCTIONS ----------------
def create_route(city_list):
    return random.sample(city_list, len(city_list))


def crossover(parent1, parent2):
    start = random.randint(0, len(parent1)-1)
    end = random.randint(start, len(parent1)-1)

    child = parent1[start:end]
    for city in parent2:
        if city not in child:
            child.append(city)
    return child


def mutate(route, rate=0.01):
    for i in range(len(route)):
        if random.random() < rate:
            j = random.randint(0, len(route)-1)
            route[i], route[j] = route[j], route[i]
    return route


# ---------------- MAIN PROGRAM ----------------
city_list = [City(random.randint(0,200), random.randint(0,200)) for _ in range(20)]

population_size = 100
generations = 200

population = [create_route(city_list) for _ in range(population_size)]
progress = []

for gen in range(generations):
    ranked = sorted(population, key=lambda r: Fitness(r).distance)
    best_distance = Fitness(ranked[0]).distance
    progress.append(best_distance)

    new_population = ranked[:10]   # elitism

    while len(new_population) < population_size:
        p1 = random.choice(ranked[:50])
        p2 = random.choice(ranked[:50])
        child = crossover(p1, p2)
        new_population.append(mutate(child))

    population = new_population

    print(f"Generation {gen+1} Distance: {best_distance:.2f}")

# ---------------- GRAPH ----------------
plt.plot(progress)
plt.xlabel("Generation")
plt.ylabel("Distance")
plt.title("Genetic Algorithm Optimization")
plt.show()

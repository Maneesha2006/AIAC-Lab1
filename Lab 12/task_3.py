import random
import matplotlib.pyplot as plt
import math

# Generate random sensor coordinates
def generate_sensors(n, width=100, height=100):
    return [(random.uniform(0, width), random.uniform(0, height)) for _ in range(n)]

# Calculate total distance of a path
def total_distance(path):
    return sum(math.dist(path[i], path[(i + 1) % len(path)]) for i in range(len(path)))

# Greedy algorithm
def greedy_path(sensors):
    unvisited = sensors[:]
    path = [unvisited.pop(0)]
    while unvisited:
        next_point = min(unvisited, key=lambda p: math.dist(path[-1], p))
        path.append(next_point)
        unvisited.remove(next_point)
    return path

# Genetic Algorithm
def genetic_algorithm(sensors, population_size=100, generations=200, mutation_rate=0.05):
    def create_individual(): return random.sample(sensors, len(sensors))
    def crossover(p1, p2):
        start, end = sorted(random.sample(range(len(p1)), 2))
        child = p1[start:end]
        child += [p for p in p2 if p not in child]
        return child
    def mutate(individual):
        if random.random() < mutation_rate:
            i, j = random.sample(range(len(individual)), 2)
            individual[i], individual[j] = individual[j], individual[i]
    population = [create_individual() for _ in range(population_size)]
    for _ in range(generations):
        population.sort(key=total_distance)
        next_gen = population[:10]
        while len(next_gen) < population_size:
            p1, p2 = random.sample(population[:50], 2)
            child = crossover(p1, p2)
            mutate(child)
            next_gen.append(child)
        population = next_gen
    return population[0]

# Plot paths
def plot_paths(random_path, greedy_path, ga_path):
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))
    titles = ['Random Path', 'Greedy Path', 'Genetic Algorithm Path']
    paths = [random_path, greedy_path, ga_path]
    for ax, path, title in zip(axs, paths, titles):
        x, y = zip(*path + [path[0]])
        ax.plot(x, y, marker='o')
        ax.set_title(f"{title}\nDistance: {total_distance(path):.2f}")
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
    plt.tight_layout()
    plt.show()

# Main execution
if __name__ == "__main__":
    sensors = generate_sensors(30)
    random_path = random.sample(sensors, len(sensors))
    greedy = greedy_path(sensors)
    ga = genetic_algorithm(sensors)
    plot_paths(random_path, greedy, ga)
import random
from lab4_homework_func import fitness_fn_positive

p_mutation = 0.2
num_of_generations = 100


def genetic_algorithm(population, fitness_fn, minimal_fitness):
    for generation in range(num_of_generations):
        print(f"Generation {generation}:")
        print_population(population, fitness_fn)

        new_population = set()

        for _ in range(len(population)):
            mother, father = random_selection(population, fitness_fn)
            child = reproduce(mother, father)

            if random.uniform(0, 1) < p_mutation:
                child = mutate(child)

            new_population.add(tuple(child))

        population = population.union(new_population)

        fittest_individual = get_fittest_individual(population, fitness_fn)

        if minimal_fitness <= fitness_fn(fittest_individual):
            print(f"\n✅ Solution found in generation {generation}!")
            break

    print(f"\nFinal generation {generation}:")
    print_population(population, fitness_fn)

    return fittest_individual


def print_population(population, fitness_fn):
    for individual in population:
        fitness = fitness_fn(individual)
        print(f"{individual} - fitness: {fitness}")


def reproduce(mother, father):
    child = mother.copy()
    crossover_point = random.randint(0, len(mother) - 1)
    for i in range(crossover_point, len(mother)):
        child[i] = father[i]
    return child


def mutate(individual):
    mutation = individual.copy()
    mutation_point = random.randint(0, 7)
    mutation[mutation_point] = random.randint(0, 7)
    return mutation


def random_selection(population, fitness_fn):
    ordered_population = list(population)
    fitness_population = sorted(
        [(e, fitness_fn(e)) for e in ordered_population],
        key=lambda x: x[1],
        reverse=True
    )

    if len(fitness_population) < 2:
        raise ValueError("Not enough individuals to select two parents.")

    return list(fitness_population[0][0]), list(fitness_population[1][0])


def get_fittest_individual(iterable, func):
    return max(iterable, key=func)


def get_initial_population(n, count):
    return set([
        tuple(random.randint(0, 7) for _ in range(n))
        for _ in range(count)
    ])


def main():
    minimal_fitness = 28  # Perfect fitness for 8 queens
    initial_population = get_initial_population(8, 4)

    fittest = genetic_algorithm(initial_population, fitness_fn_positive, minimal_fitness)
    print("\n🎯 Fittest Individual:", fittest)
    print("🎯 Fitness:", fitness_fn_positive(fittest))


if __name__ == '__main__':
    main()

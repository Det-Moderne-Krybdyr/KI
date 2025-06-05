import random


p_mutation = 0.2
num_of_generations = 30


def genetic_algorithm(population, fitness_fn, minimal_fitness):
    for generation in range(num_of_generations):
        print("Generation {}:".format(generation))
        print_population(population, fitness_fn)

        new_population = set()

        for i in range(len(population)):
            mother, father = random_selection(population, fitness_fn)
            child = reproduce(mother, father)

            if random.uniform(0, 1) < p_mutation:
                child = mutate(child)

            new_population.add(tuple(child))

        # Add new population to population, use union to disregard
        # duplicate individuals
        population = set(population).union(new_population)

        fittest_individual = get_fittest_individual(population, fitness_fn)

        if minimal_fitness <= fitness_fn(fittest_individual):
            break

    print("Final generation {}:".format(generation))
    print_population(population, fitness_fn)

    return fittest_individual


def print_population(population, fitness_fn):
    for individual in population:
        fitness = fitness_fn(individual)
        print("{} - fitness: {}".format(individual, fitness))


def reproduce(mother, father):
    """
    Reproduce two individuals with single-point crossover
    Return the child individual
    """
    print("mother:" + str(mother))
    child = mother.copy()
    crossover_point = random.randint(0, 2)

    for i in range(crossover_point, 3):
        child[i] = father[i]

    return child


def mutate(individual):
    mutation_point = random.randint(0, 2)
    mutation = individual.copy()
    mutation[mutation_point] = 1 - mutation[mutation_point]  # Flip bit
    return mutation


def random_selection(population, fitness_fn):
    """
    Compute fitness of each in population according to fitness_fn and add up
    the total. Then choose 2 from sequence based on percentage contribution to
    total fitness of population
    Return selected variable which holds two individuals that were chosen as
    the mother and the father
    """

    # Python sets are randomly ordered. Since we traverse the set twice, we
    # want to do it in the same order. So let's convert it temporarily to a
    # list.
    ordered_population = list(population)
    fitness_population = [(e, fitness_fn(e)) for e in ordered_population]
    fitness_population.sort(key=lambda x: x[1], reverse=True)

    if len(fitness_population) < 2:
        raise ValueError(
            "Not enough individuals in the population to select two parents."
        )

    return list(fitness_population[0][0]), list(fitness_population[1][0])


def fitness_function(individual):
    return sum(bit * (2**i) for i, bit in enumerate(reversed(individual)))


def get_fittest_individual(iterable, func):
    return max(iterable, key=func)


def get_initial_population(n, count):
    """
    Randomly generate count individuals of length n
    Note since its a set it disregards duplicate elements.
    """
    return set([tuple(random.randint(0, 1) for _ in range(n)) for _ in range(count)])


def main():
    minimal_fitness = 7

    # Curly brackets also creates a set, if there isn't a colon to indicate a dictionary
    initial_population = {(1, 1, 0), (0, 0, 0), (0, 1, 0), (1, 0, 0)}
    # initial_population = get_initial_population(3, 4)

    fittest = genetic_algorithm(initial_population, fitness_function, minimal_fitness)
    print("Fittest Individual: " + str(fittest))


if __name__ == "__main__":
    pass
    main()

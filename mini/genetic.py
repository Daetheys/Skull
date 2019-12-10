"""
START
Generate the initial population
Compute fitness
REPEAT
    Selection
    Crossover
    Mutation
    Compute fitness
UNTIL population has converged
STOP
"""


import random


# Modifiy these parameters
size = 4  # Affects the size of the population
rounds = 16  # Number of rounds disputed with each opponent
limiter = 16  # Affects the maximum percentage of mutation
generations = 64  # Number of generations created

sm1 = size - 1  # Rational players quotient
population_size = 2 * (size ** 4)  # A hypercube because we have 4 parameters


def rational_player(n):
    return ([((n // (size ** 3)) % size) / sm1,
            ((n // (size ** 2)) % size) / sm1,
            ((n // size) % size) / sm1, (n % size) / sm1])


def random_player():
    return ([random.random(), random.random(),
            random.random(), random.random()])


def first_generation():
    tab = []
    for n in range(population_size // 2):
        tab.append(rational_player(n))
        tab.append(random_player())
    return tab


def one_game(p1, p2, focus):
    cards = ['', '']
    bid1, bid2 = -1, -1
    if (random.random() < p1[0]):
        cards[0] = 'skull'
    else:
        cards[0] = 'flower'
    if (random.random() < p2[1]):
        cards[1] = 'skull'
    else:
        cards[1] = 'flower'
    if (cards[0] == 'skull' or random.random() < p1[2]):
        bid1 = 1
        if (cards[1] == 'flower' and random.random() < p2[3]):
            bid2 = 2
    else:
        bid1 = 2
    if (bid1 > bid2):
        if (cards[0] == 'skull'):
            return -1 * focus
        elif (bid1 == 1):
            return 1 * focus
        elif (cards[1] == 'flower'):
            return 1 * focus
        else:
            return -1 * focus
    else:
        if (cards[0] == 'skull'):
            return 1 * focus
        else:
            return -1 * focus


def fitness(player, opps):
    win = 0
    for opp in opps:
        for g in range(rounds):
            win += one_game(player, opp, 1) + one_game(opp, player, -1)
    return win


def accumulate(fit):
    a = [0] * len(fit)
    a[0] = fit[0]
    for i in range(1, len(fit)):
        a[i] = a[i-1] + fit[i]
    return a, a[len(a) - 1]


def selection(acc, maxi):
    r = random.random() * maxi
    i = 0
    while (acc[i] < r):
        i += 1
    return i


def best_player(gen, fit):
    b, p = fit[0], 0
    for i in range(1, len(fit)):
        if (fit[i] > b):
            p = i
            b = fit[p]
    print(gen[p])
    print(b)


def run_genetic():
    opponents = first_generation()
    gen = first_generation()
    fit = [fitness(p, opponents) for p in gen]
    for z in range(generations):
        acc, maxi = accumulate(fit)
        children = []
        for i in range(population_size // 2):
            parent1 = gen[selection(acc, maxi)]
            parent2 = gen[selection(acc, maxi)]
            child1, child2 = [0, 0, 0, 0], [0, 0, 0, 0]
            for j in range(4):
                if (random.randint(0, 1) == 0):
                    child1[j] = parent1[j]
                    child2[j] = parent2[j]
                else:
                    child1[j] = parent2[j]
                    child2[j] = parent1[j]
            children.append(child1)
            children.append(child2)
        for i in range(population_size):
            for j in range(4):
                mutation = (random.random() - 0.5) / limiter
                children[i][j] += mutation
                children[i][j] = max(min(children[i][j], 1), 0)
        gen = children
        fit = [fitness(p, opponents) for p in gen]
        best_player(gen, fit)

import random
import time
import pandas as pd

from deap import base
from deap import creator
from deap import tools

# Pandas file
distances_df = pd.read_excel("Project3_DistancesMatrix.xlsx", index_col=0)
# mudar para índices
distances = distances_df.copy()
distances = distances.reset_index(drop=True)
distances.columns = range(1, len(distances.columns) + 1)
N_POINTS_COLUMNS = len(distances.columns)
N_POINTS_ROWS = len(distances)
N_POINTS = N_POINTS_ROWS
M_POINT_IN = N_POINTS - 1
#print(len(distances))
print(distances)
print

# Functions
# Evaluation function
def evalTSP(individual):
    distance_calc = 0
    for i in range(N_POINTS):
        distance_calc = distance_calc + distances[individual((i+1)%M_POINT_IN)][individual(i)]
    return sum(individual),

# Code
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
# Attribute generator 
toolbox.register("attr_int", random.randint, 1, N_POINTS)
# Structure initializers
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_int, 100)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evalTSP)
toolbox.register("mate", tools.cxTwoPoint) #cxTwoPoint
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05) # indpb = 0.05
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    pop = toolbox.population(n=300)

    # Evaluate the entire population
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    # CXPB is the probability with which two individuals
    # are crossed
    #
    # MUTPB is the probability for mutating an individual
    CXPB, MUTPB = 0.5, 0.2
    
    # Extracting all the fitnesses of 
    fits = [ind.fitness.values[0] for ind in pop]

    # Variable keeping track of the number of generations
    g = 0

    # Count the time
    start_time = time.time()
    # Begin the evolution
    while max(fits) < 100 and g < 100: # g < 1000
        # A new generation
        g = g + 1
        print("-- Generation %i --" % g)
        # Select the next generation individuals
        offspring = toolbox.select(pop, len(pop))
        # Clone the selected individuals
        offspring = list(map(toolbox.clone, offspring))
        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values
        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        pop[:] = offspring
        # Gather all the fitnesses in one list and print the stats
        fits = [ind.fitness.values[0] for ind in pop]

        length = len(pop)
        mean = sum(fits) / length
        sum2 = sum(x*x for x in fits)
        std = abs(sum2 / length - mean**2)**0.5

        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))
        print("  Avg %s" % mean)
        print("  Std %s" % std)

    end_time  = time.time()
    algo_time = end_time - start_time
    print("Algotithm execution time:", algo_time)

if __name__ == "__main__":
    main()
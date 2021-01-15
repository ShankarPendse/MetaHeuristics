"""
Author: Shankar Pendse
file: TestTSP_R00195877.py
"""

from TSP_R00195877 import *
import argparse
import time

eval_configurations = {1: [1000, 0.001, 800, "random", "order1", "inverse"],
                       2: [1000, 0.001, 800, "random", "uniform", "scramble"],
                       3: [300, 0.05, 800, "random", "order1", "scramble"],
                       4: [300, 0.05, 800, "random", "uniform", "inverse"],
                       5: [1000, 0.001, 800, "NN", "order1", "scramble"],
                       6: [300, 0.05, 800, "NN", "uniform", "inverse"]}


def run_ga(config, fname, best_fitness):
    pop_size = eval_configurations[int(config)][0]
    mut_rate = eval_configurations[int(config)][1]
    max_iter = eval_configurations[int(config)][2]
    ini_genr = eval_configurations[int(config)][3]
    crs_over = eval_configurations[int(config)][4]
    mut_meth = eval_configurations[int(config)][5]

    print("        Initializing population using {} method\n".format(ini_genr))
    init_start_time = time.process_time()
    ga = BasicTSP(fname, pop_size, mut_rate, max_iter, ini_genr, crs_over, mut_meth)
    init_end_time = time.process_time()
    print("        Initialization complete in {} seconds\n".format(init_end_time - init_start_time))
    print("        Searching for better solution:\n")
    ga.search()
    best_fitness.append(ga.best.getFitness())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("config")
    parser.add_argument("file_name")
    parser.add_argument("iterations")
    args = parser.parse_args()

    print("config: ", args.config)
    print("fname: ", args.file_name)
    print("iterations: ", args.iterations)

    best_fitness = []  # stores best fitness for each iteration of the specified configuration
    print("\nRunning GA for config : {}".format(args.config))
    start_time = time.process_time()
    for iteration in range(int(args.iterations)):
        print("\n  Iteration: {}".format(iteration+1))
        run_ga(args.config, args.file_name, best_fitness)
    end_time = time.process_time()
    print("\n  Mean fitness for above configuration is: ", np.mean(np.array(best_fitness)))
    print("  Median fitness for above configuration is: ", np.median(np.array(best_fitness)))
    print("  Fittest solution is: ", np.min(np.array(best_fitness)))
    print("\nTime taken to run config {} for {} iterations is: {} seconds".format(args.config, args.iterations, end_time-start_time))

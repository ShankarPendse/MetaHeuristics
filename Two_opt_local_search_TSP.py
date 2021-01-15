import numpy as np
import random
import time
import math
import argparse

random.seed(195877)


class TSP2opt:
    def __init__(self, _fname, _variant):
        self.fname = _fname
        # self.ini_genr = _ini_genr
        self.data = {}
        self.tour =[]
        self.min_distances = []
        self.start_city = {}
        self.cities = 0
        self.cost = 0
        self.best_move = []
        self.variant = _variant
        self.costs_list = []
        self.best_costs_list = []
        self.times = 1

        self.readInstance()
        for t in range(self.times):
            print("---------------------------------------------------------------------------------------------------")
            print("\nRunning {} version of 2-opt Local search for {} times on {} file: \n".format(self.variant, t + 1,
                                                                                                  self.fname))
            self.initPopulation()
            if self.variant == "basic":
                self.basicTwoOptTSP()
            elif self.variant == "variant1":
                self.variant1TwoOptTSP()
            elif self.variant == "variant2":
                self.variant2TwoOptTSP()
        self.display_stats()

    def readInstance(self):
        """
        Reading an instance from fName
        """
        file = open(self.fname, 'r')
        self.cities = int(file.readline())
        self.data = {}
        for line in file:
            (cid, x, y) = line.split()
            self.data[int(cid)] = (int(x), int(y))
        file.close()

    def initPopulation(self):
        # Generating a tour at random
        # if self.ini_genr == "random":
        self.tour = list(self.data.keys())
        random.shuffle(self.tour)
        self.cost = self.computeCost()
        print("initial tour is: ", self.tour)
        print("\n  no of cities visited: ", len(self.tour))
        print("  Initial cost is: ", self.cost)

    def display_stats(self):
        print("-------------------------------------------------------------------------------------------------------")
        print("Stats for the 2-OPT Algorithm, variant: ", self.variant)
        # print("Type of Algorithm: ", self.variant)
        print("\n  Min value of all the best costs computed: ", np.min(self.best_costs_list))
        print("\n  Max value of all the best costs computed: ", np.max(self.best_costs_list))
        print("\n  Mean value of all the best costs computed: ", np.mean(self.best_costs_list))
        print("\n  Median value of all the best costs computed: ", np.median(self.best_costs_list))
        print("\n  Standard deviation of all the best costs computed: ", np.std(self.best_costs_list))
        print("\n  Coefficient of variation of all the best costs computed: ",
              np.std(self.best_costs_list) / np.mean(self.best_costs_list))

    def euclideanDistance(self, c1, c2):
        """
        Distance between two cities
        """
        d1 = self.data[c1]
        d2 = self.data[c2]
        return math.sqrt((d1[0] - d2[0]) ** 2 + (d1[1] - d2[1]) ** 2)

    def computeCost(self):
        # cost of the total tour, including the distance travelled from last city to the first city
        distance = self.euclideanDistance(self.tour[0], self.tour[len(self.tour) - 1])
        for i in range(0, len(self.tour) - 1):
            distance += self.euclideanDistance(self.tour[i], self.tour[i + 1])
        return round(distance, 4)

    def swapCost(self, indices):
        # Function to calculate the additive and subtractive costs and return the updated cost for the move specified by the indices
        cost = self.cost
        cost -= self.euclideanDistance(self.tour[indices[0]-1], self.tour[indices[0]]) + self.euclideanDistance(self.tour[indices[1]], self.tour[indices[1]+1])
        cost += self.euclideanDistance(self.tour[indices[0]-1], self.tour[indices[1]]) + self.euclideanDistance(self.tour[indices[0]], self.tour[indices[1]+1])
        return round(cost, 4)

    def updateTour(self, new_cost):
        # Swap the edges as per the best_move values and assign new_cost value to the tour updated
        self.tour[self.best_move[0]+1:self.best_move[1]] = self.tour[self.best_move[0]+1:self.best_move[1]][::-1]
        # Below line can be uncommented and last line can be commented to calculate the cost again and compare the results to verify
        # self.cost = self.computeCost()
        self.cost = new_cost

    # Basic 2 opt local search algorithm
    def basicTwoOptTSP(self):
        # best_costs_list = []
        start_time = time.process_time()
        not_opt = True
        n = len(self.tour)
        while not_opt:
            not_opt = False
            i = 0
            curr_best = self.cost
            while i < n-2:
                j = i + 2
                while j < n:
                    new_cost = self.swapCost([i + 1, j - 1])
                    if new_cost < curr_best:
                        self.best_move = [i, j]
                        curr_best = new_cost
                        not_opt = True
                    j += 1
                i += 1
            if not_opt:
                # Updating the best move
                self.updateTour(curr_best)
                print("    Best move: {}, New cost: {}".format(self.best_move, self.cost))
        end_time = time.process_time()
        self.best_costs_list.append(self.cost)
        print("    Best solution obtained from 2opt algorithm is:", self.cost)
        print("    opt_cost: ", self.cost)
        print("    no of cities visited: ", len(self.tour))
        print("    Time taken to find best solution: {} seconds".format(end_time - start_time))

    # Variant1 of 2-opt Algorithm
    def variant1TwoOptTSP(self):
        max_iterations = 10000  # Setting maximum number of tries to come out of the execution as we get stuck in local optima
        n = len(self.tour)
        start_time = time.process_time()
        for iteration in range(max_iterations):
            opt = False
            random_ind = random.randint(1, n-2)  # Selecting a random index as a vertex of the edge
            edge_ind = [random_ind, random_ind+1]  # Defining the edge
            curr_best = self.cost
            i = 0
            while i < n:
                if abs(i - edge_ind[0]) >= 2 and abs(i - edge_ind[1]) >= 2:  # Skipping the indices where there won't be any swap
                    indices = sorted([i] + edge_ind)  # Reordering the indices as the distance is symmetric
                    new_cost = self.swapCost([indices[0]+1, indices[-1]-1])
                    if new_cost < curr_best:
                        self.best_move = [indices[0], indices[-1]]
                        curr_best = new_cost
                        opt = True
                i += 1
            if opt:
                # Updating the best move
                self.updateTour(curr_best)
                print("    Iteration: {} Best move: {}, New cost: {}".format(iteration, self.best_move, self.cost))
        end_time = time.process_time()
        self.best_costs_list.append(self.cost)
        print("    Best solution obtained from 2opt algorithm is:", self.cost)
        print("    opt_cost: ", self.cost)
        print("    no of cities visited: ", len(self.tour))
        print("    Time taken to find best solution: {} seconds".format(end_time - start_time))
        print("\n  Total time taken for {} iterations is: {} seconds".format(max_iterations, end_time - start_time))

    # Variant2 of 2-opt Algorithm
    def variant2TwoOptTSP(self):
        max_iterations = 10000
        n = len(self.tour)
        start_time = time.process_time()
        for iteration in range(max_iterations):
            random_ind = random.randint(1, n-2)
            edge_ind = [random_ind, random_ind+1]
            curr_best = self.cost
            i = 0
            while i < n:
                if abs(i - edge_ind[0]) >= 2 and abs(i - edge_ind[1]) >= 2:  # Skipping the indices where there won't be any swap
                    indices = sorted([i] + edge_ind)
                    new_cost = self.swapCost([indices[0]+1, indices[-1]-1])
                    if new_cost < curr_best:
                        self.best_move = [indices[0], indices[-1]]
                        curr_best = new_cost
                        # Applying the first improvement and breaking the loop for the selected random edge
                        self.updateTour(new_cost)
                        print("    Iteration: {} Best move: {}, New cost: {}".format(iteration, self.best_move, self.cost))
                        break
                i += 1
        end_time = time.process_time()
        self.best_costs_list.append(self.cost)
        print("\n  Total time taken for {} iterations is: {} seconds".format(max_iterations, end_time - start_time))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name")
    # parser.add_argument("ini_genr")
    parser.add_argument("algo")
    args = parser.parse_args()

    print("FileName: ", args.file_name)
    # print("TourGeneration: ", args.ini_genr)
    print("Variant: ", args.algo)
    # TSP = TSP2opt(args.file_name, args.ini_genr, args.algo)
    TSP = TSP2opt(args.file_name, args.algo)
    # TSP = TSP2opt("inst-6.tsp", "random", "variant1")

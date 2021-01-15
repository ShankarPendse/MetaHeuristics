"""
Basic TSP Example
file: Individual.py
Modified where ever required as per the logic
"""

import random
import math
import numpy as np
import sys

sys.setrecursionlimit(10000)

myStudentNum = 195877
random.seed(myStudentNum)


class Individual:
    def __init__(self, _size, _data, cgenes, initpoptype):
        """
        Parameters and general variables
        """
        self.fitness    = 0
        self.genes      = []
        self.genSize    = _size
        self.data       = _data
        self.initpoptype = initpoptype
        self.count = 0

        if self.initpoptype == "random":
            if cgenes:  # Child genes from crossover
                self.genes = cgenes
            else:   # Random initialisation of genes
                self.genes = list(self.data.keys())
                random.shuffle(self.genes)
        else:
            if cgenes:  # Child genes from crossover
                self.genes = cgenes
            else:   # nearest neighbour initialisation of genes
                # print("NN Execution")
                self.min_distances = []
                self.start_city = self.choose_start_city()
                # print("start_city: ", self.start_city)
                self.current_city = self.start_city
                data = self.data.copy()
                self.nearest_neighbor_insertion(data)

    # This method is used while initializing the population using nearest neighbour insertion heuristic
    def choose_start_city(self):
        start_city_id = random.choice(list(self.data))
        return {start_city_id: self.data[start_city_id]}

    # This method implements the actual nearest neighbour insertion logic
    def nearest_neighbor_insertion(self, data):
        [start_city_id] = self.current_city.keys()
        start_city_coordinates = np.array(list(self.current_city.values()))
        self.genes.append(start_city_id)

        del data[start_city_id]

        if len(data) == 0:
            self.return_to_start_city()
        else:
            while len(data) > 0:
                remaining_city_coordinates = np.array(list(data.values()))
                remaining_city_ids = np.array(list(data.keys()))

                distances = np.linalg.norm(start_city_coordinates - remaining_city_coordinates, axis=1)

                self.min_distances.append(np.min(distances))
                min_dist_ind = np.argmin(distances)

                # next_city_coordinates = remaining_city_coordinates[min_dist_ind]
                next_city_id = remaining_city_ids[min_dist_ind]
                next_start_city = {next_city_id: data[next_city_id]}

                self.current_city = next_start_city
                self.nearest_neighbor_insertion(data)

    # Once all cities are visited, sales man will return to the city from where he started
    def return_to_start_city(self):
        current_city_coordinates = np.array(list(self.current_city.values()))
        first_city_cordinates = np.array(list(self.start_city.values()))

        self.min_distances.append(np.linalg.norm(current_city_coordinates - first_city_cordinates))
        self.current_city = self.start_city
        self.fitness = np.sum(self.min_distances)

    def copy(self):
        """
        Creating a copy of an individual
        """
        ind = Individual(self.genSize, self.data, self.genes[0:self.genSize], self.initpoptype)
        ind.fitness = self.getFitness()
        return ind

    # Calculates the euclidean distance between given two cities
    def euclideanDistance(self, c1, c2):
        """
        Distance between two cities
        """
        d1 = self.data[c1]
        d2 = self.data[c2]
        return math.sqrt((d1[0]-d2[0])**2 + (d1[1]-d2[1])**2)

    # Returns the fitness of an individual
    def getFitness(self):
        return self.fitness

    # This method will be used to compute the fitness of an individual
    def computeFitness(self):
        """
        Computing the cost or fitness of the individual
        """
        self.fitness    = self.euclideanDistance(self.genes[0], self.genes[len(self.genes)-1])
        for i in range(0, self.genSize-1):
            self.fitness += self.euclideanDistance(self.genes[i], self.genes[i+1])

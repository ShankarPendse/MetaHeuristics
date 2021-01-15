"""
Author: Shankar Pendse
file: Experimental_TSP_R00195877.py
"""
import random
import plotly.graph_objects as go
from Individual import *

sys.setrecursionlimit(10000)

myStudentNum = 195877
random.seed(myStudentNum)


class BasicTSP:
    def __init__(self, _fName, _popSize, _mutationRate, _maxIterations, _ini_genr, _crs_over, _mut_meth):
        """
        Parameters and general variables
        """
        self.population = []
        self.matingPool = []
        self.best = None
        self.popSize = _popSize
        self.genSize = None
        self.mutationRate = _mutationRate
        self.maxIterations = _maxIterations
        self.iteration = 0
        self.fName = _fName
        self.data = {}
        self.ini_genr = _ini_genr
        self.crs_over = _crs_over
        self.mut_meth = _mut_meth
        self.best_iterations = []
        self.best_fitnesses = []

        self.pop_fitness = []
        self.pop_avg_fitness = []
        self.pop_median_fitness = []
        self.pop_best_fitness = []

        self.readInstance()
        self.initPopulation()

    # updates the data dictionary of the object
    def readInstance(self):
        """
        Reading an instance from fName
        """
        file = open(self.fName, 'r')
        self.genSize = int(file.readline())
        self.data = {}
        for line in file:
            (cid, x, y) = line.split()
            self.data[int(cid)] = (int(x), int(y))
        file.close()

    # Creating initial population using the specified method and updating the fittest individual as best
    def initPopulation(self):
        for i in range(0, self.popSize):
            individual = Individual(self.genSize, self.data, [], self.ini_genr)
            # Computing fitness for random initialization here, for Nearest neighbor, it will be done automatically
            if self.ini_genr == "random":
                individual.computeFitness()
            self.population.append(individual)

        self.best = self.population[0].copy()
        for ind_i in self.population:
            if self.best.getFitness() > ind_i.getFitness():
                self.best = ind_i.copy()
        print("        Best Initial Solution: ", self.best.getFitness())

    # Making a copy of the best available individual
    def updateBest(self, candidate):
        if self.best == None or candidate.getFitness() < self.best.getFitness():
            self.best = candidate.copy()
            print("        iteration: ", self.iteration, "best: ", self.best.getFitness())
            self.best_iterations.append(self.iteration)
            self.best_fitnesses.append(self.best.getFitness())

    def binaryTournamentSelection(self):
        """
        Binary tournament selection implementation
        selects 4 individuals at random from mating pool
        create 2 pairs at random
        return the best individual from each pair as parents
        """
        individuals = random.sample(self.matingPool, k=4)
        pair1 = random.sample(individuals, k=2)
        pair2 = random.sample(individuals, k=2)

        parent1 = pair1[0] if pair1[0].getFitness() <= pair1[1].getFitness() else pair1[1]
        parent2 = pair2[0] if pair2[0].getFitness() <= pair2[1].getFitness() else pair2[1]

        return [parent1, parent2]

    def uniformCrossover(self, indA, indB):
        """
        Uniform Crossover Implementation
        """
        child1_genes = [None] * self.genSize
        child2_genes = [None] * self.genSize

        # Selecting 1/4th of genes to remain in their original position
        random_indices = random.sample(range(self.genSize), k=int(self.genSize / 4))

        # Positions where the genes won't change
        for i in random_indices:
            child1_genes[i] = indA.genes[i]
            child2_genes[i] = indB.genes[i]

        # Appending remaining genes from indB to child1_genes in the order they appear in indB
        index = 0
        for gene in indB.genes:
            if gene not in child1_genes:
                while child1_genes[index] is not None:
                    index += 1
                child1_genes[index] = gene
                index += 1

        # Appending remaining genes from indA to child2_genes in the order they appear in indA
        index = 0
        for gene in indA.genes:
            if gene not in child2_genes:
                while child2_genes[index] is not None:
                    index += 1
                child2_genes[index] = gene
                index += 1

        child1 = Individual(self.genSize, self.data, child1_genes, self.ini_genr)
        child2 = Individual(self.genSize, self.data, child2_genes, self.ini_genr)

        child1.computeFitness()
        child2.computeFitness()

        # Returning best among the two children created
        return child1 if child1.fitness < child2.fitness else child2

    def order1Crossover(self, indA, indB):
        """
        Order-1 Crossover Implementation
        """

        # Selecting two indices at random
        random_indices = random.sample(range(self.genSize), k=2)
        start_index = min(random_indices)
        end_index = max(random_indices)


        genes_indA = indA.genes[start_index : end_index+1]
        genes_indB = indB.genes[start_index : end_index+1]

        # Placing all the genes from indB except those which are in genes_indA
        child1_genes = [gene for gene in indB.genes if gene not in genes_indA]
        # Appending the genes in genes_indA at the end of the child
        child1_genes.extend(genes_indA)

        # Placing all the genes from indA except those which are in genes_indB
        child2_genes = [gene for gene in indA.genes if gene not in genes_indB]
        # Appending the genes in genes_indB at the end of the child
        child2_genes.extend(genes_indB)

        child1 = Individual(self.genSize, self.data, child1_genes, self.ini_genr)
        child2 = Individual(self.genSize, self.data, child2_genes, self.ini_genr)

        child1.computeFitness()
        child2.computeFitness()

        # Returning best among the two children created
        return child1 if child1.fitness < child2.fitness else child2

    def scrambleMutation(self, ind):
        """
        Scramble Mutation implementation
        """
        if random.random() > self.mutationRate:
            return

        # Selecting two random indices in the range 0 to genSize
        random_indices = random.sample(range(self.genSize), k=2)
        start_index = min(random_indices)
        end_index = max(random_indices)
        no_of_genes_shuffle = end_index - start_index

        # Shuffling the genes between the randomly selected indices
        ind.genes[start_index:end_index + 1] = random.sample(ind.genes[start_index:end_index + 1], k=no_of_genes_shuffle + 1)

    def inversionMutation(self, ind):
        """
        Inversion Mutation implementation
        """
        if random.random() > self.mutationRate:
            return

        # Selecting two random indices in the range 0 to genSize
        random_indices = random.sample(range(self.genSize), k=2)
        start_index = min(random_indices)
        end_index = max(random_indices)

        # Reversing the order of genes between the selected indices
        ind.genes[start_index: end_index + 1] = ind.genes[start_index: end_index + 1][::-1]

    def updateMatingPool(self):
        """
        Updating the mating pool before creating a new generation
        """
        self.matingPool = []
        for ind_i in self.population:
            self.matingPool.append(ind_i.copy())

    def newGeneration(self):
        """
        Creating a new generation
        1. Selection
        2. Crossover
        3. Mutation
        """
        for i in range(0, len(self.population)):
            """
            1. Select two candidates using Binary Tournament selection process
            2. Apply Crossover (either order 1 or uniform order based)
            3. Apply Mutation (either inverse or scramble)
            """

            # Selection of parents via Binary Tournament Selection process
            parent1, parent2 = self.binaryTournamentSelection()

            # This check is necessary to avoid crossover with itself
            while parent1.genes == parent2.genes:
                parent1, parent2 = self.binaryTournamentSelection()

            # Performing specified crossover and mutation
            if self.crs_over == "order1":
                child_crossover = self.order1Crossover(parent1, parent2)
                if self.mut_meth == "inverse":
                    self.inversionMutation(child_crossover)
                elif self.mut_meth == "scramble":
                    self.scrambleMutation(child_crossover)
                child_crossover.computeFitness()
                self.updateBest(child_crossover)
                self.population[i] = child_crossover

            if self.crs_over == "uniform":
                child_crossover = self.uniformCrossover(parent1, parent2)
                if self.mut_meth == "inverse":
                    self.inversionMutation(child_crossover)
                elif self.mut_meth == "scramble":
                    self.scrambleMutation(child_crossover)
                child_crossover.computeFitness()
                self.updateBest(child_crossover)
                self.population[i] = child_crossover

            self.pop_fitness.append(self.population[i].fitness)

        self.pop_avg_fitness.append(np.mean(self.pop_fitness))
        self.pop_median_fitness.append(np.median(self.pop_fitness))
        self.pop_best_fitness.append(self.best.fitness)

    def GAStep(self):
        """
        One step in the GA main algorithm
        1. Updating mating pool with current population
        2. Creating a new Generation
        """
        self.updateMatingPool()
        self.newGeneration()

    def search(self):
        """
        General search template.
        Iterates for a given number of steps
        """
        self.iteration = 0
        while self.iteration < self.maxIterations:
            self.GAStep()
            self.iteration += 1

        print("\n        Total iterations: ", self.iteration)
        print("        Best Solution: ", self.best.getFitness())
        print("        Best solution's Gene size:", self.best.genSize)
        print("Mating pool size: ", len(self.matingPool))
        if len(self.best_fitnesses) > 1:
            self.visualize()
        self.visualize_popfitness()

    # Method to visualize the convergence of fitness for each of the best individual obtained at different iterations
    def visualize(self):
        fig = go.Figure(data = go.Scatter(x = self.best_iterations, y = self.best_fitnesses, mode = 'lines+markers'))
        fig.update_layout(title = 'Genetic Algorithm Performance, config:(popSize: {}, mut_rate: {}, iterations: {}, crs_over: {}, mut_meth: {})'.format(self.popSize, self.mutationRate, self.maxIterations, self.crs_over, self.mut_meth),
                          xaxis_title = 'Iterations',
                          yaxis_title = "Fitness (Distance Travelled)")
        fig.show()

    # Method to visualize how population fitness varies with mean and median fitness of entire population over max_iterations
    def visualize_popfitness(self):
        xvalues = [i for i in range(self.maxIterations)]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=xvalues, y=self.pop_best_fitness, mode='lines+markers', name="Best Fitness"))
        fig.add_trace(go.Scatter(x=xvalues, y=self.pop_avg_fitness, mode='lines+markers', name="Avg Fitness"))
        fig.add_trace(go.Scatter(x=xvalues, y=self.pop_median_fitness, mode='lines+markers', name="Median Fitness"))
        fig.update_layout(title='Genetic Algorithm Inside works, config:(popSize: {}, mut_rate: {}, iterations: {},'
                                'crs_over: {}, mut_meth: {})'.format(self.popSize, self.mutationRate,
                                                                     self.maxIterations, self.crs_over, self.mut_meth),
                          xaxis_title='Iterations',
                          yaxis_title="Fitness (Distance Travelled)")
        fig.show()

import random
from Queens import *
import matplotlib.pyplot as plt
import sys
import time
import numpy as np
import math

studentNum = 195877
# random.seed(studentNum)

class HillClimbing:
    def __init__(self, _size, _maxIterations, _maxRestarts):
        self.bCost = 0
        self.maxIterations = _maxIterations
        self.maxRestarts = _maxRestarts
        self.gIteration = 0
        self.nRestart = 0
        self.iteration = 0
        self.size = _size
        self.q = Queens(self.size)
        self.bCost = -1
        self.cHistory = []
        self.cBHistory = []
        self.iHistory = []

    def solveMaxMin(self):
        candidate_sol = self.q.generateRandomState(self.size)
        self.bCost = self.q.getHeuristicCost(candidate_sol)
        self.iteration = -1

        while self.iteration < self.maxIterations and self.bCost > 0:
            self.gIteration += 1
            self.iteration += 1
            self.cBHistory.append(self.bCost)
            self.cHistory.append (self.q.getHeuristicCost(candidate_sol))
            self.iHistory.append(self.gIteration)

            max_candidate = []
            max_cost = -1
            # Find queen involved in max conflicts
            for cand_i in range(0, self.size):
                cost_i = self.q.getHeuristicCostQueen(candidate_sol, cand_i)
                if max_cost < cost_i:
                    max_cost = cost_i
                    max_candidate = [cand_i]
                elif max_cost == cost_i:
                    # Ties
                    max_candidate.append(cand_i)

            if max_cost == -1:
                break
            candidate = max_candidate[ random.randint(0, len(max_candidate)-1) ]
            old_val = candidate_sol[candidate]

            ##best move for the selected queen
            min_cost = max_cost
            best_pos = []

            for pos_i in range(0, self.size):
                if pos_i == old_val:
                    # Neighbor must be different to current
                    continue
                candidate_sol[candidate] = pos_i
                cost_i = self.q.getHeuristicCostQueen(candidate_sol, candidate)
                if min_cost > cost_i:
                    min_cost = cost_i
                    best_pos = [pos_i]
                # elif min_cost == cost_i:
                #     # Note this will allow sideways moves
                #     best_pos.append(pos_i)
            if best_pos:
                # Some non-worsening move found
                candidate_sol[candidate] = best_pos[ random.randint(0, len(best_pos)-1) ]
                cost_i = self.q.getHeuristicCost(candidate_sol)
            else:
                # Put back previous sol if no improving solution
                candidate_sol[candidate]=old_val
            if self.bCost > cost_i:
                self.bCost = cost_i
        return (candidate_sol, self.bCost)

    def solveWithRestarts(self, solve, maxR):
        res = solve()
        self.nRestart = 0
        if res[1] == 0:
            # print ("   Restart: ",self.nRestart, "Cost: ",res[1], "Iter: ",self.iteration, self.gIteration)
            return res
        else:
            while self.nRestart < maxR and res[1] > 0:
                self.nRestart +=1
                res = solve()
            #     print ("   Restart: ",self.nRestart, "Cost: ",res[1], "Iter: ",self.iteration, self.gIteration)
            # print ("   Restart: ",self.nRestart, "Cost: ",res[1], "Iter: ",self.iteration, self.gIteration)
            return res

    # Method to plot the Run time distributions
    def runTimeDistributions(self, solved_run_times, search_steps, runs):
        solved_cumulative_run_times = np.cumsum(solved_run_times)
        solved_cumulative_search_steps = np.cumsum(search_steps)

        run_time_of_j = list()

        j = np.argsort(solved_cumulative_run_times)
        for ele in j:
            run_time_of_j.append(solved_cumulative_run_times[ele])

        j_over_k = [ele / runs for ele in j]

        plt.figure(1)
        plt.plot(run_time_of_j, j_over_k)
        # plt.plot(np.log1p(run_time_of_j), j_over_k)
        # plt.plot(run_time_of_j, np.log1p(j_over_k))
        plt.xlabel("rt(j)")
        plt.ylabel("j/k")
        plt.grid(b=True, which='major', color='#666666', linestyle='-')
        plt.title("Run Time Distributions")

        plt.figure(2)
        plt.plot(solved_cumulative_search_steps, j_over_k)
        # plt.plot(np.log1p(solved_cumulative_search_steps), j_over_k)
        # plt.plot(solved_cumulative_search_steps, np.log1p(j_over_k))
        plt.xlabel("Search Steps")
        plt.ylabel("j/k")
        plt.grid(b=True, which='major', color='#666666', linestyle='-')
        plt.title("Run Time Distributions")

        plt.show()


if __name__ == "__main__":
    n, iters, restarts = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    solved_runs = []
    solved_run_times = []
    search_steps = []
    run_start_time = time.process_time()

    runs = 200
    for i in range(runs):
        random.seed(studentNum * i * 100)
        hc = HillClimbing(n,iters,restarts)
        start_time = time.process_time()
        sol = hc.solveWithRestarts(hc.solveMaxMin, hc.maxRestarts)
        end_time = time.process_time()
        if sol[1] == 0:
            solved_runs.append(i+1)
            solved_run_times.append(end_time - start_time)
            search_steps.append(hc.gIteration)
            print("\nRun : {}".format(i + 1))
            print("cost: ", sol[1])
            print("Time taken: ", end_time - start_time)
            print("Cumulative run time: ", end_time - run_start_time)
    run_end_time = time.process_time()

    print("\nTotal time taken for 200 runs: ", run_end_time - run_start_time)
    print("\nsolved_runs: ", solved_runs)

    hc.runTimeDistributions(solved_run_times, search_steps, runs)

# MetaHeuristics
This repository will be used for solving the Lab exercises and assignments that were assigned during the Master's course in AI
This readme will be updated with details of all the codes that will be uploaded

# TSP.py and it's description is as below:

1) TSP.py: This is a solution to the Travelling salesman problem, which uses nearest neighbor insertion method.
   This script takes two parameters, 1. input file name which has the city ID x-coordinates y-coordinates (for all the cities under consideration)
                                     2. output file name, which will have the total distance travelled as first line and the city ids that are visited in order.
                                     
                                     
   Minimum distances are calculated using Euclidian distance method
   

2) TSP_Final.py: This is a solution to the Travelling salesman problem using 3 different approaches: 1) Nearest Neighbor insertion, 2) Heuristic Insertion and 3) Random tour generation. This code accepts one parameter which is a input file which contains total number of cities in the first line and city_id X_coordinates Y_coordinates in the following lines (seperated by whitespace). This assumes that all city ids and coordinates are provided in the input file

   ### How to execute the file from command prompt:> python TSP_Final.py inputfilename
   
# Methods of file TSP_R00195877.py:
1.	__init__: Apart from the default parameters, I am passing 3 new parameters: 
a.	_ini_genr: Determines how the initial set of population is generated (could be “random” for random generation of tours or “NN” for Nearest Neighbor insertion heuristics)
b.	_crs_over: Determines which cross over method to be called. (Could be either “order1” for order-1 Crossover and “uniform” for Uniform order based Crossover)
c.	_mut_meth: Determines which mutation method to be called. (Could be either “inverse” for Inverse mutation or “scramble” for Scramble mutation)
2.	readInstance(self): There is no change to this method, used as it is, which will read the file passed and update genSize and data variables accordingly

3.	initPopulation(self): This will create the individuals as many as specified in _popSize parameter depending on the _ini_genr value (either “random” or “NN”)

4.	updateBest(self): Used as it is without any change. This will create a copy of fittest individual in the population

5.	binaryTournamentSelection(self): A typical implementation of binary tournament selection procedure, where 4 individuals are selected at random from mating pool, create 2 pairs at random and return the fittest parent from each pair

6.	uniformCrossOver(self): Implements the uniform Crossover method. This method creates and returns only one child

7.	order1Crossover(self): Implements the order1Crossover method. This method creates and returns only one child

8.	scrambleMutation(self): Implements the scramble Mutation 

9.	inverseMutation(self): Implements the inverse Mutation 

10.	updateMatingPool(self): No change to this method, using the default one as it was supplied. This method updates the mating pool for each iteration

11.	newGeneration(self): This will call the methods binaryTournamentSelection, use the returned parents for performing specified crossover (self.crs_over) and pass on the result of crossover to specified mutation method (self.mut_meth). After performing selection, crossover and mutation, we will calculate the fitness (by calling computeFitness method defined in the module Individual.py) of resulting individual and call updateBest method to update the best solution. This process is done for whole population size for each iteration

12.	GAStep(self): This one is used without any change (used as is from the provided code), which first updates the matingPool with the population by calling updateMatingPool(self) method and then calls newGeneration(self) method. These two methods are called in sequence (one after the other)

13.	Search(self): This will call the method GAStep(self) for self.max_iterations times

# Methods of file Experimental_TSP_R00195877.py:
	No new methods are added to this file when compared to “TSP_R00195877.py” module, only change is in the implementation logic for uniformCrossOver and order1CrossOver. Instead of creating and returning one child, these methods in this module will create two children and return the fittest among them. Rest all logic remains same as in “TSP_R00195877.py” module. In this way we are biasing our population towards the fittest individual, to update the mating pool at each iteration.

Please look into below to know how to run the modules to get the same results as presented in the report:
1) Source code files included:
1.	Individual.py
2.	TSP_R00195877.py
3.	Experimental_TSP_R00195877.py
4.	TestTSP_R00195877.py
5.	EvaluationTSP_R00195877.py

First two files are imported as modules in the last two files
1)	TestTsp_R00195877.py is used to run the basic configuration by importing the module TSP_R00195877.py
2)	TestTsp_R00195877.py is also used to run the Experimental part by importing the module Experimental_TSP_R00195877.py
3)	EvaluationTSP_R00195877.py can be used to play around with the configuration dictionary specified in this file, to change population size, mutation rate and max_iterations
2) Requirements: numpy, plotly graph objects, argparse
3) How to run the code: please refer to the Requirements above
Place all the source code files and data files in the same folder

### For exact commands to run, please refer below:

All below commands are executed in PyCharm IDE in windows OS

Run time could be different depending on the machine configuration.

All source code files and data files are assumed to be in the same directory

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Conditions for error free exeuction:
-------------------------------------
	1. number of arguments passed should be exactly 3 (which configuration to run, file name and how many times we want to run that configuration for)
	2. First argument helps in choosing the configuration to be run. It must be passed as an integer and it must be between 1 and 6 (both inclusive)
	3. Second argument must be a file name
	4. Third argument specifies how many times we want to run the configuration specified in Frist argument. It must an integer

Failing to meet above conditions will result in error
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

Open the terminal navigatet to the path where all files are placed and execute below commands one by one or run any command at random:
-------------------------------------------------------

# FOR SECTION1 of the Report (R00195877_REPORT.pdf):

python TestTSP_R00195877.py 1 inst-4.tsp 1
python TestTSP_R00195877.py 1 inst-16.tsp 1
python TestTSP_R00195877.py 1 inst-6.tsp 1

python TestTSP_R00195877.py 2 inst-4.tsp 1
python TestTSP_R00195877.py 2 inst-16.tsp 1
python TestTSP_R00195877.py 2 inst-6.tsp 1

python TestTSP_R00195877.py 3 inst-4.tsp 1
python TestTSP_R00195877.py 3 inst-16.tsp 1
python TestTSP_R00195877.py 3 inst-6.tsp 1

python TestTSP_R00195877.py 4 inst-4.tsp 1
python TestTSP_R00195877.py 4 inst-16.tsp 1
python TestTSP_R00195877.py 4 inst-6.tsp 1

python TestTSP_R00195877.py 5 inst-4.tsp 1
python TestTSP_R00195877.py 5 inst-16.tsp 1
python TestTSP_R00195877.py 5 inst-6.tsp 1

python TestTSP_R00195877.py 6 inst-4.tsp 1
python TestTSP_R00195877.py 6 inst-16.tsp 1
python TestTSP_R00195877.py 6 inst-6.tsp 1

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# For SECTION2 of the Report (R00195877_REPORT.pdf):

python EvaluationTSP_R00195877.py 1 inst-4.tsp 1
python EvaluationTSP_R00195877.py 2 inst-4.tsp 1
python EvaluationTSP_R00195877.py 3 inst-4.tsp 1
python EvaluationTSP_R00195877.py 4 inst-4.tsp 1
python EvaluationTSP_R00195877.py 5 inst-4.tsp 1
python EvaluationTSP_R00195877.py 6 inst-4.tsp 1

For this we have to update the "eval_configurations" dictionary defined in the file "EvaluationTSP_R00195877.py" as per required settings

eval_configurations" dictionary key values represents the configuration number, and value for each key is a list of 
[popSize, mutation_probability, max_iterations, pop_initialization_method, crossover, mutation] in the order

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# For SECTION3 of the Report (R00195877_REPORT.pdf):

python TestTSP_R00195877.py 1 inst-4.tsp 5
python TestTSP_R00195877.py 2 inst-4.tsp 5
python TestTSP_R00195877.py 3 inst-4.tsp 5
python TestTSP_R00195877.py 4 inst-4.tsp 5
python TestTSP_R00195877.py 5 inst-4.tsp 5
python TestTSP_R00195877.py 6 inst-4.tsp 5


&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# For SECTION4 of the Report (R00195877_REPORT.pdf) :

Before running below commands, make sure we are importing the module
Experimental_TSP_R00195877.py instead of TSP_R00195877.py (we can just comment and uncomment the import sections in the file TestTSP_R00195877.py)


python TestTSP_R00195877.py 1 inst-4.tsp 1
python TestTSP_R00195877.py 1 inst-16.tsp 1
python TestTSP_R00195877.py 1 inst-6.tsp 1

python TestTSP_R00195877.py 2 inst-4.tsp 1
python TestTSP_R00195877.py 2 inst-16.tsp 1
python TestTSP_R00195877.py 2 inst-6.tsp 1

python TestTSP_R00195877.py 3 inst-4.tsp 1
python TestTSP_R00195877.py 3 inst-16.tsp 1
python TestTSP_R00195877.py 3 inst-6.tsp 1

python TestTSP_R00195877.py 4 inst-4.tsp 1
python TestTSP_R00195877.py 4 inst-16.tsp 1
python TestTSP_R00195877.py 4 inst-6.tsp 1

python TestTSP_R00195877.py 5 inst-4.tsp 1
python TestTSP_R00195877.py 5 inst-16.tsp 1
python TestTSP_R00195877.py 5 inst-6.tsp 1

python TestTSP_R00195877.py 6 inst-4.tsp 1
python TestTSP_R00195877.py 6 inst-16.tsp 1
python TestTSP_R00195877.py 6 inst-6.tsp 1



&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# For SECTION 1 part of the report (R00195877_REPORT.pdf):
To run the basic asked configurations please use below command:
>> python TestTSP_R00195877.py <config number> <filename> <iterations>
•	Config number must be any one from [1,2,3,4,5,6] 
•	Filename : tsp instance file name
•	Iterations: how many times we want to run the specified config

# For SECTION 2 part of the report (R00195877_REPORT.pdf):
To Evaluate the performance of GA, please use below command:
>> python EvaluationTSP_R00195877.py <config number> <filename> <iterations>
•	Config number must be any one from [1,2,3,4,5,6] 
•	Filename : tsp instance file name
•	Iterations: how many times we want to run the config
•	Note: Please make sure to alter the configuration dictionary in the file EvaluationTSP_R00195877.py as required to alter the values of population size, mutation rate and max_iterations

# For SECTION3 part of the report (R00195877_REPORT.pdf) :
To Analyse the performance over of GA on each configuration run over 5 times use below command:
	>> python TestTSP_R00195877.py <config number> <filename> <iterations>
•	Config number must be any one from [1,2,3,4,5,6] 
•	Filename : tsp instance file name
•	Iterations: how many times we want to run the specified config
For SECTION4 part of the report
To run the experiment part of the report, please use below command:
a.	>> python TestTSP_R00195877.py <config number> <filename> <iterations>
i.	config number any one from [1,2,3,4,5,6] as as asked in the assessment document
ii.	filename : tsp instance file name
iii.	iterations: how many times we want to run the config
Note: Please make sure to import the module Experimental_TSP_R00195877.py instead of TSP_R00195877.py (you can just comment and uncomment the import sections in the file TestTSP_R00195877.py)

Dictionary Configurations:

1.	"eval_configurations" dictionary defined in the file "EvaluationTSP_R00195877.py" as per required settings

eval_configurations" dictionary key values represents the configuration number, and value for each key is a list as mentioned below 
[popSize, mutation_probability, max_iterations, pop_initialization_method, 
crossover, mutation]

2.	“basic_configurations” dictionary defined in the file “TestTSP_R00195877.py” defines the basic configurations as it is asked in the assignment

“basic_configurations " dictionary key values represents the configuration number, and value for each key is a list as mentioned below 
[popSize, mutation_probability, max_iterations, pop_initialization_method, 
crossover, mutation]

# ####################################################################################################################################################################

1.	TSP 2OPT LOCAL SEARCH:
Place the supplied .py files and data files in same directory. To see the same results as presented in the report, please use the files inst-4.tsp, inst-16.tsp and inst-6.tsp. Please do not alter the random seed if you want to see the same results as depicted in the report (Pendse_Shankar_R00195877_MH2)

This can be run from command prompt (terminal/pycharm terminal) as follows:

1)	Two_opt_local_search_TSP.py “filename” “basic”
This command will run the basic version of 2-opt algorithm on the specified file name, with random initialization of the tour.

2)	Two_opt_local_search_TSP.py “filename” “variant1”
This command will run the first variant of 2-opt algorithm on the specified file name, with random initialization of the tour

3)	Two_opt_local_search_TSP.py “filename” “variant2”
This command will run the second variant of 2-opt algorithm on the specified file name, with random initialization of the tour

By default, all the execution happens for 1 time, if you want to run it for more than 1 time, please open the file two_opt_ls_v1_4.py, change the assignment value of self.times = 1 , on line number 24



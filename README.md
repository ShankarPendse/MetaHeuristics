# MetaHeuristics
This repository will be used for solving the Lab exercises and assignments that were assigned during the Master's course in AI
This readme will be updated with details of all the codes that will be uploaded

# First file in this repository is TSP.py and description is as below:

1) TSP.py: This is a solution to the Travelling salesman problem, which uses nearest neighbor insertion method.
   This script takes two parameters, 1. input file name which has the city ID x-coordinates y-coordinates (for all the cities under consideration)
                                     2. output file name, which will have the total distance travelled as first line and the city ids that are visited in order.
                                     
                                     
   Minimum distances are calculated using Euclidian distance method
   

2) TSP_Final.py: This is a solution to the Travelling salesman problem using 3 different approaches: 1) Nearest Neighbor insertion, 2) Heuristic Insertion and 3) Random tour generation. This code accepts one parameter which is a input file which contains total number of cities in the first line and city_id X_coordinates Y_coordinates in the following lines (seperated by whitespace). This assumes that all city ids and coordinates are provided in the input file

   ### How to execute the file from command prompt:> python TSP_Final.py inputfilename

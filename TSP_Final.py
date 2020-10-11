import random
import numpy as np
import argparse
import sys

sys.setrecursionlimit(1500)


class TravellingSalesMan:
    def __init__(self, file_name):
        self.file_name = file_name
        self.visited_city_ids = []
        self.visited_city_coordinates = []
        self.min_distances = []
        self.data = self.read_data(file_name)
        self.no_of_cities = len(self.data)
        self.start_city = self.choose_start_city()
        self.current_city = self.start_city
        self.tot_distance_travelled = 0

    def read_data(self, file_name):
        data = {}
        print(file_name)
        with open(file_name) as f:
            next(f)
            for line in f:
                line = line.split()
                data[int(line[0])] = list(map(int, line[1:]))
        return data

    def choose_start_city(self):
        start_city_id = random.choice(list(self.data))
        print("Randomly choosen start_city : ", {start_city_id: self.data[start_city_id]})
        return {start_city_id: self.data[start_city_id]}

    def nearest_neighbor_insertion(self):
        if len(self.visited_city_ids) == self.no_of_cities:
            self.__init__(self.file_name)

        [start_city_id] = self.current_city.keys()
        start_city_coordinates = np.array(list(self.current_city.values()))
        self.visited_city_ids.append(start_city_id)

        del self.data[start_city_id]

        if len(self.data) == 0:
            print("Nearest Neighbor Insertion completed and the order of cities visited: ", self.visited_city_ids)
            print("Returning to the city from where it all started")
            self.return_to_start_city()
        else:
            while len(self.data) > 0:
                remaining_city_coordinates = np.array(list(self.data.values()))
                remaining_city_ids = np.array(list(self.data.keys()))

                distances = np.linalg.norm(start_city_coordinates - remaining_city_coordinates, axis=1)

                self.min_distances.append(np.min(distances))
                min_dist_ind = np.argmin(distances)

                next_city_coordinates = remaining_city_coordinates[min_dist_ind]
                next_city_id = remaining_city_ids[min_dist_ind]
                next_start_city = {next_city_id: self.data[next_city_id]}

                self.current_city = next_start_city
                self.nearest_neighbor_insertion()

    def heuristic_insertion(self, index=0):
        if len(self.visited_city_ids) == self.no_of_cities:
            self.__init__(self.file_name)

        present_city = self.current_city
        [present_city_id] = list(self.current_city)
        [present_city_coordinates] = np.array(list(self.current_city.values()))

        # print("current_city: ", present_city)
        # print("current_city_id: ", present_city_id)
        # print("current_city_coordinates: ", present_city_coordinates)

        if (len(self.visited_city_ids) == 0) or (len(self.visited_city_ids) == 1):
            self.visited_city_ids.append(present_city_id)
            self.visited_city_coordinates.append(present_city_coordinates)
        else:
            self.visited_city_ids.insert(index + 1, present_city_id)
            self.visited_city_coordinates.insert(index + 1, present_city_coordinates)

        # print("current_tour_ids: ", self.visited_city_ids)
        # print("current_tour_coordinates: ", self.visited_city_coordinates)

        del self.data[present_city_id]

        if len(self.data) == 0:
            print("Heuristic Insertion completed and the order of cities visited: ", self.visited_city_ids)
            print("Returning to the city from where it all started")
            self.return_to_start_city()
        else:
            while len(self.data) > 0:
                next_city_id = random.choice(list(self.data))
                next_city = {next_city_id: self.data[next_city_id]}
                next_city_coordinates = np.array(list(next_city.values()))

                # print("next_city: ", next_city)
                # print("nexct_city_id: ", next_city_id)
                # print("next_city_coordinates", next_city_coordinates)

                distances = np.linalg.norm(next_city_coordinates - self.visited_city_coordinates, axis=1)
                # print("distances: ", distances)
                self.min_distances.append(np.min(distances))
                min_distance_index = np.argmin(distances)
                # print("min_distance_index: ", min_distance_index)
                self.current_city = next_city
                self.heuristic_insertion(min_distance_index)

    def random_tour(self):
        if len(self.visited_city_ids) == self.no_of_cities:
            self.__init__(self.file_name)

        [current_city_id] = list(self.current_city)
        current_city_coordinates = np.array(list(self.current_city.values()))
        # print("current_city_id: ", current_city_id)
        self.visited_city_ids.append(current_city_id)

        del self.data[current_city_id]

        if len(self.data) == 0:
            print("Random tour completed and the order of cities visited: ", self.visited_city_ids)
            print("Returning to the city from where it all started")
            self.return_to_start_city()
        else:
            while len(self.data) > 0:
                next_city_id = random.choice(list(self.data))
                next_city = {next_city_id: self.data[next_city_id]}
                next_city_coordinates = np.array(list(next_city.values()))

                # print("randomly chosen next city: ", next_city_id)
                # print("current city coordinates: ", current_city_coordinates)
                # print("next_city_coordinates: ", next_city_coordinates)

                distance = np.linalg.norm(current_city_coordinates - next_city_coordinates)

                # print("distance between current and next city: ", distance)

                self.min_distances.append(distance)
                self.current_city = next_city
                self.random_tour()

    def return_to_start_city(self):
        current_city_coordinates = np.array(list(self.current_city.values()))
        first_city_cordinates = np.array(list(self.start_city.values()))

        self.min_distances.append(np.linalg.norm(current_city_coordinates - first_city_cordinates))
        self.current_city = self.start_city
        # self.tot_distance_travelled = self.calculate_tot_distance_travelled()
        self.tot_distance_travelled = np.sum(self.min_distances)
        print("Returned to the start city, current city is {} which is same as start city {}".format(self.current_city, self.start_city))
        print("Total distance travelled is: ", self.tot_distance_travelled)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file_name")
    args = parser.parse_args()

    tsp = TravellingSalesMan(args.input_file_name)
    print("\n Solving the problem using Nearest Neighbor Insertion technique")
    print("--------------------------------------------------------------")

    tsp.nearest_neighbor_insertion()

    print("**************************************************************")
    print("\n Solving the problem using Heuristic Insertion technique")
    print("--------------------------------------------------------------")

    tsp.heuristic_insertion()

    print("**************************************************************")
    print("\n Solving the problem using Random generation of tour")
    print("--------------------------------------------------------------")

    tsp.random_tour()

    print("**************************************************************")
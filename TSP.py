import random
import numpy as np
import argparse


class TravellingSalesMan:
    def __init__(self, file_name):
        self.visited_city_ids = []
        self.min_distances = []
        self.data = self.read_data(file_name)
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
        [start_city_id] = self.current_city.keys()
        start_city_coordinates = np.array(list(self.current_city.values()))
        self.visited_city_ids.append(start_city_id)

        del self.data[start_city_id]

        if len(self.data) == 0:
            # Returning to the city from where it all started
            current_city_coordinates = np.array(list(self.current_city.values()))
            first_city_cordinates = np.array(list(self.start_city.values()))

            self.min_distances.append(np.linalg.norm(current_city_coordinates - first_city_cordinates))
            self.current_city = self.start_city
            self.tot_distance_travelled = self.calculate_tot_distance_travelled()

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

    def calculate_tot_distance_travelled(self):
        return np.sum(self.min_distances)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file_name")
    parser.add_argument("output_file_name")
    args = parser.parse_args()

    print("Initializing the object which also reads the data and randomly chooses the starting city")
    tsp = TravellingSalesMan(args.input_file_name)
    print("Solving Travelling salesman problem using Nearest Neighbor insertion")
    tsp.nearest_neighbor_insertion()
    print("Starting location : ", tsp.start_city)
    print("current location: ", tsp.current_city)
    print("Order of cities in which they are visited: ", tsp.visited_city_ids)
    print("Total distance travelled: ", tsp.tot_distance_travelled)
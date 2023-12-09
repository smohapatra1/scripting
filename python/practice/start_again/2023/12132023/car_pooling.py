# #   https://leetcode.com/problems/car-pooling/

# 1094. Car Pooling
# Medium
# 4.3K
# 89
# Companies
# There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

# You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

# Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 

# Example 1:

# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false
# Example 2:

# Input: trips = [[2,1,5],[3,3,7]], capacity = 5
# Output: true

from typing import List
def CarPooling(trips: List[List[int]], capacity: int )-> bool:
    path = [0]* 1000
    for nums, a, b in trips:
        for loc in range(a,b):
            path[loc] +=nums
            if path[loc] > capacity:
                return False
    return True

if __name__ == "__main__":
    trips = [[2,1,5],[3,3,7]]
    capacity = 4
    print ("{}".format(CarPooling(trips, capacity)))
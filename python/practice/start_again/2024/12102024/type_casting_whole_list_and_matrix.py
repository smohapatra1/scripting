#   https://www.geeksforgeeks.org/python-type-casting-whole-list-and-matrix/

import numpy as np

test_list = [1, 4, 9, 10, 19]
test_matrix = [[5, 6, 8], [8, 5, 3], [9, 10, 3]]
cast_list = np.array(test_list, dtype=str)
cast_matrix = np.array(test_matrix, dtype=str)
print ("The list after type casting : ", str(cast_list))
print ("The Matrix after type casting : \n", str(cast_matrix))

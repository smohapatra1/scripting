#   https://www.geeksforgeeks.org/python-append-at-front-and-remove-from-rear/

import numpy as np

test_array = np.array([4, 5, 7, 3, 10])
print ("Original list : ", test_array)
res = np.concatenate(([13], np.delete(test_array,- 1)))
print ("New list      : ", res)
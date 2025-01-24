#   https://www.geeksforgeeks.org/python-sort-by-frequency-of-second-element-in-tuple-list/?ref=ml_lbp

import numpy as np
def SecondList(test_list):
    arr = np.array(test_list)
    counts = np.unique(arr[:, 1 ], return_counts=True)
    sorted_indices = np.argsort(-counts[1])
    sorted_arr = np.empty_like(arr)
    start = 0
    for i in sorted_indices:
        freq = counts[1][i]
        indices = np.where(arr[:, 1] == counts[0][i])[0]
        end = start + freq
        sorted_arr[start:end] = arr[indices]
        start = end
    res = [tuple(row) for row in sorted_arr]
    return res

if __name__ == "__main__":
    test_list = [(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]
    print ("Original list :", test_list)
    print ("Sorted List   :", SecondList(test_list))
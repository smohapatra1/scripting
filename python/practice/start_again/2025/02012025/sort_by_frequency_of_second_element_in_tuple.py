#   https://www.geeksforgeeks.org/python-sort-by-frequency-of-second-element-in-tuple-list/?ref=ml_lbp

from collections import defaultdict
def SortByFreq(test_list):
    freq_map = defaultdict(int)
    for idx, val in test_list:
        freq_map[val] += 1
    res = sorted(test_list, key= lambda ele: freq_map[ele[1]], reverse = True)
    return res

if __name__ == "__main__":
    test_list = [(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]
    print ("Unsorted : ", test_list)
    print ("Sorted   : ",  SortByFreq(test_list))

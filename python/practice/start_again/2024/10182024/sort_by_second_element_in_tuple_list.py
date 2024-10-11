#   https://www.geeksforgeeks.org/python-sort-by-frequency-of-second-element-in-tuple-list/
from collections import Counter

def Sorted(test_list):
    print ("Current list : " + str(test_list))
    temp = Counter(val for key, val in test_list)
    res = sorted(test_list, key=lambda ele: temp[ele[1]], reverse=True)
    return res
if __name__ == "__main__":
    test_list = [(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]
    print ("List after sorting ", Sorted(test_list))
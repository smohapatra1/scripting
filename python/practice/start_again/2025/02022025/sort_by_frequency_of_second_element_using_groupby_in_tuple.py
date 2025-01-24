#   https://www.geeksforgeeks.org/python-sort-by-frequency-of-second-element-in-tuple-list/?ref=ml_lbp

from itertools import groupby
def SecondList(test_list):
    freq = {val: len(list(group)) for val, group in groupby(sorted(test_list, key=lambda x: x[1]), lambda x: x[1])}  
    return sorted(test_list, key=lambda x: freq[x[1]], reverse=True)

if __name__ == "__main__":
    test_list = [(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]
    print ("Original list :", test_list)
    print ("Sorted List   :", SecondList(test_list))
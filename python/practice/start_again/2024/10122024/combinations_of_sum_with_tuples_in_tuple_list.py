#   https://www.geeksforgeeks.org/python-combinations-of-sum-with-tuples-in-tuple-list/

from itertools import combinations
def Combinations(test_list):
    res = [(b1 + a1, b2 + a2) for (a1, a2) , (b1, b2) in combinations(test_list, 2)]
    return res

if __name__ == "__main__":
    test_list = [(2, 4), (6, 7), (5, 1), (6, 10)]
    result = Combinations(test_list)
    print (result)
#   https://www.geeksforgeeks.org/python-convert-tuple-matrix-to-tuple-list/
from itertools import chain

def TupleMatrix(test_list):
    # # Solution - 01 
    # temp = [ele for sub in test_list for ele in sub]
    # res = list(zip(*temp))
    # return res
    # Solution - 02 
    return list(zip(*chain.from_iterable(test_list)))


if __name__ == "__main__":
    test_list = [[(4, 5), (7, 8)], [(10, 13), (18, 17)], [(0, 4), (10, 1)]]
    result = TupleMatrix(test_list)
    print (result)
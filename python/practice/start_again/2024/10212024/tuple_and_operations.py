#   https://www.geeksforgeeks.org/python-and-operation-between-tuples/

from operator import and_
import operator
def AndOperations(test_tup1, test_tup2):
    # Solution - 01 
    # res = tuple(map(and_, test_tup1, test_tup2))
    # Solution - 02
    res = tuple(map(operator.iand, test_tup1, test_tup2))
    return res

if __name__ == "__main__":
    test_tup1 = (10, 4, 5)
    test_tup2 = (2, 5, 18)
    print ("AND operations on Tuples = ", AndOperations(test_tup1, test_tup2))
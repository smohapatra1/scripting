#   https://www.geeksforgeeks.org/python-elementwise-and-in-tuples/
import operator

def ElementTuple(test_tup1, test_tup2):
    # Solution - 01 
    # res = tuple(ele1 & ele2 for ele1, ele2 in zip(test_tup1, test_tup2))
    # Solution - 02 
    res = tuple(map(operator.iand, test_tup1, test_tup2))
    return res

if __name__ == "__main__":
    test_tup1 = (10, 4, 6, 9) 
    test_tup2 = (5, 2, 3, 3)
    print ("Elementwise And = ", ElementTuple(test_tup1, test_tup2))
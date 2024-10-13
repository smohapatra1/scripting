#   https://www.geeksforgeeks.org/python-tuple-xor-operation/
from operator import xor

def XOR(test_tup1, test_tup2):
    # Solution = 01 
    # res = tuple(ele1 ^ ele2 for ele1, ele2 in zip(test_tup1, test_tup2))
    # Solution = 02 
    res = tuple(map(xor, test_tup1, test_tup2))
    return res

if __name__ == "__main__":
    test_tup1 = (10, 4, 6, 9) 
    test_tup2 = (5, 2, 3, 3) 
    print ("XOR operations = ", XOR(test_tup1, test_tup2))
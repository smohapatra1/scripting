#   https://www.geeksforgeeks.org/python-modulo-of-tuple-elements/

def Modulo(test_tup1, test_tup2):
    res = tuple(ele1 % ele2 for ele1 , ele2 in zip(test_tup1, test_tup2))
    return res 

if __name__ == "__main__":
    test_tup1 = (10, 4, 5, 6)
    test_tup2 = (5, 6, 7, 5)
    result = Modulo(test_tup1, test_tup2)
    print (result)
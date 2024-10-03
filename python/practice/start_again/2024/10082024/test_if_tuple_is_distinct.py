#   https://www.geeksforgeeks.org/python-test-if-tuple-is-distinct/

def TestDistinct(test_tup):
    res = len(set(test_tup)) == len(test_tup)
    return res


if __name__ == "__main__":
    # test_tup = (1, 4, 5, 6, 1, 4) 
    test_tup = (1, 4, 5, 6)
    result = TestDistinct(test_tup)
    print (result)
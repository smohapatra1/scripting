#   https://www.geeksforgeeks.org/python-flatten-tuple-of-list-to-tuple/

def Flatten(test_tuple):
    res = tuple(sum(test_tuple, []))
    return res

if __name__ == "__main__":
    test_tuple = ([5, 6], [6, 7, 8, 9], [3])
    result = Flatten(test_tuple)
    print (result)
#   https://www.geeksforgeeks.org/python-removing-duplicates-from-tuple/

def Duplicate(test_tup):
    res = tuple(set(test_tup))
    return res
if __name__ == "__main__":
    test_tup = (1, 3, 5, 2, 3, 5, 1, 1, 3)
    result = Duplicate(test_tup)
    print (result)
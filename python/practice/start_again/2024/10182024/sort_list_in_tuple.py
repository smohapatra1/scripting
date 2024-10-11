#   https://www.geeksforgeeks.org/python-sort-lists-in-tuple/

def Sorted(test_tup):
    print ("Tuples before sorted : " + str(test_tup))
    res = tuple(sorted(sub) for sub in test_tup)
    return res


if __name__ == "__main__":
    test_tup = ([7, 5, 4], [8, 2, 4], [0, 7, 5])
    print ("Tuples after sorted  : ", Sorted(test_tup))
#   https://www.geeksforgeeks.org/python-remove-nested-records-from-tuple/

def NestedTuple(test_tup):
    res = []
    for i in test_tup:
        if not type(i) is tuple:
            res.append(i)
    res = tuple(res)
    return res

if __name__ == "__main__":
    test_tup = (1, 5, 7, (4, 6), 10)
    result = NestedTuple(test_tup)
    print (result)
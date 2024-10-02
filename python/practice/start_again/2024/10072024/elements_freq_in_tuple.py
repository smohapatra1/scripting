#   https://www.geeksforgeeks.org/python-elements-frequency-in-tuple/

from collections import defaultdict

def FreqTuple(test_tup):
    res = defaultdict(int)
    for ele in test_tup:
        res[ele] +=1
    return str(dict(res))


if __name__ == "__main__":
    test_tup = (4, 5, 4, 5, 6, 6, 5, 5, 4)
    result = FreqTuple(test_tup)
    print (result)
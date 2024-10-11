#   https://www.geeksforgeeks.org/python-elements-frequency-in-mixed-nested-tuple/

from collections import Counter

def NestedTuple(test_tuple):
    for tup in test_tuple:
        if isinstance(tup, tuple):
            yield from NestedTuple(tup)
        else:
            yield tup

if __name__ == "__main__":
    test_tuple = (5, 6, (5, 6), 7, (8, 9), 9, 10)
    res = dict(Counter(NestedTuple(test_tuple)))
    print (res)
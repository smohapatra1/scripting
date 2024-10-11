#   https://www.geeksforgeeks.org/python-how-to-get-unique-elements-in-nested-tuple/
from itertools import chain
def Unique(test_list):
    res = set(chain.from_iterable(test_list))
    return res

if __name__ == "__main__":
    test_list = [(3, 4, 5), (4, 5, 7), (1, 4)]
    result = Unique(test_list)
    print (result)
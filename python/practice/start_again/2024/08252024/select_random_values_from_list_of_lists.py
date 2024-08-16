#   https://www.geeksforgeeks.org/python-program-to-select-random-value-form-list-of-lists/
from itertools import chain
import random
def Random(test_list):
    res = random.choice(list(chain.from_iterable(test_list)))
    return res

if __name__ == "__main__":
    test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]
    result = Random(test_list)
    print (result)
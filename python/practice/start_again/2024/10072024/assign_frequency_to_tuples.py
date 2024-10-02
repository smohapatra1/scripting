#   https://www.geeksforgeeks.org/python-assign-frequency-to-tuples/
from collections import Counter

def Freq(test_list):
    res = [(*key, val ) for key, val in Counter(test_list).items()]
    return res


if __name__ == "__main__":
    test_list = [(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9, ), (2, 7)]
    result = Freq(test_list)
    print (result)
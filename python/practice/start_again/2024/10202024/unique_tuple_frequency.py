# https://www.geeksforgeeks.org/python-unique-tuple-frequency-order-irrespective/

def TupleFreq(test_list):
    res = len(list(set(tuple(sorted(sub)) for sub in test_list)))
    return res

if __name__ == "__main__":
    test_list = [(3, 4), (1, 2), (4, 3), (5, 6)]
    result = TupleFreq(test_list)
    print (result)
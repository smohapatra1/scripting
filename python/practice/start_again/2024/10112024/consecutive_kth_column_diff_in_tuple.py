#       https://www.geeksforgeeks.org/python-consecutive-kth-column-difference-in-tuple-list/


def consecutive(test_list, K ):
    res = []
    for idx in range(0, len(test_list) - 1 ):
        res.append(abs(test_list[idx][K] - test_list[idx+1][K]))
    return res


if __name__ == "__main__":
    test_list = [(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)]
    K = 1 
    result = consecutive(test_list, K )
    print (result)
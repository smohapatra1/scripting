#   https://www.geeksforgeeks.org/python-remove-consecutive-k-element-records/

def RemoveConsecutive(test_list, K):
    res = []
    for i in test_list:
        skip = False
        for j in range(len(i) - 1):
            if i[j] == K and i[j+1] == K :
                skip = True
                break
        if not skip:
            res.append(i)
    return res

if __name__ == "__main__":
    test_list = [(4, 5), (5, 6), (1, 3), (0, 0)]
    K = 0
    result = RemoveConsecutive(test_list, K )
    print ( result)
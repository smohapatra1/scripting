#   https://www.geeksforgeeks.org/python-join-tuples-if-similar-initial-element/

def join(test_list):
    res = []
    for sub in test_list:
        if res and res[-1][0] == sub[0]:
            res[-1].extend(sub[1:])
        else:
            res.append([ele for ele in sub])
    res = list(map(tuple, res))
    return res

if __name__ == "__main__":
    test_list = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]
    result = join(test_list)
    print (result)
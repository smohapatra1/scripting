#   https://www.geeksforgeeks.org/python-extract-elements-with-frequency-greater-than-k/

def Greater(test_list, K ):
    res = []
    for i in test_list:
        freq = test_list.count(i)
        if freq > K and i not in res:
            res.append(i)
    return res
if __name__ == "__main__":
    test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8, 8, 8, 8, 8]
    K = 3 
    result = Greater(test_list, K )
    print (result)
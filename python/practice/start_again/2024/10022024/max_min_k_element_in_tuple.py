#   https://www.geeksforgeeks.org/python-maximum-and-minimum-k-elements-in-tuple/

def MaxMin(test_tup, K ):
    test_tup = list(test_tup)
    temp = sorted(test_tup)
    res = tuple(temp[:K] + temp[-K:])
    return res

if __name__ == "__main__":
    test_tup = (5, 20, 3, 7, 6, 8)
    K = 2 
    result = MaxMin(test_tup, K)
    print (result)
#   https://www.geeksforgeeks.org/python-closest-pair-to-kth-index-element-in-tuple/

def KthIndex(test_list, K , tup):
    res = min(test_list, key=lambda x:abs(x[K-1] - tup[K-1]))
    return res
if __name__ == "__main__":
    test_list = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]
    tup = (17, 23)
    K = 1 
    result = KthIndex(test_list, K , tup)
    print (result)
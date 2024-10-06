#   https://www.geeksforgeeks.org/python-kth-column-product-in-tuple-list/

def Column(val):
    res = 1 
    for ele in val:
        res *= ele
    return res

if __name__ == "__main__":
    test_list = [(5, 6, 7), (1, 3, 5), (8, 9, 19)]
    K = 2 
    res = Column([sub[K] for sub in test_list])
    print (res)
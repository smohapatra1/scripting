#   https://www.geeksforgeeks.org/python-filter-tuples-by-kth-element-from-list/

def KthList(test_list, K ):
    check_list = [4, 2, 8, 10]
    res = [sub for sub in test_list if sub[K] in check_list]
    return res
if __name__ == "__main__":
    test_list = [("GFg", 5, 9), ("is", 4, 3), ("best", 10, 29)]
    K = 1
    result = KthList(test_list, K)
    print (result)
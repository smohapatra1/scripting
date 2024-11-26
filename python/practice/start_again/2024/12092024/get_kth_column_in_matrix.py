#   https://www.geeksforgeeks.org/python-get-kth-column-of-matrix/

def KthList(test_list):
    return [sub[K] for sub in test_list]


if __name__ == "__main__":
    test_list = [[4, 5, 6], [8, 1, 10], [7, 12, 5]]
    K = 1
    print ("Current List : ", test_list)
    print ("New list ", KthList(test_list))
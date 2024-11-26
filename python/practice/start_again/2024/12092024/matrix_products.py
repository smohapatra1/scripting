#   https://www.geeksforgeeks.org/python-matrix-product/


def prod(test_list):
    res = 1 
    for ele in test_list:
        res *= ele
    return res

if __name__ == "__main__":
    test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
    print("Result = ", prod([ele for sub in test_list for ele in sub]))
    
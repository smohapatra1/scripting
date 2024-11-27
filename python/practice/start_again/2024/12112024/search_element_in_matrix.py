#   https://www.geeksforgeeks.org/python-search-elements-in-a-matrix/

def FindMatrix(test_list, N ):
    res = any(N in sub for sub in test_list)
    return res

if __name__ == "__main__":
    test_list = [[4, 5, 6],
             [10, 2, 13],
             [1, 11, 18]]
    N = 13
    print ("Current list : ", test_list)
    print ("Finding the value in test_list ? ", (FindMatrix(test_list, N )))
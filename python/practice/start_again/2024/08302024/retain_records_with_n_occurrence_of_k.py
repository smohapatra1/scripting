#   https://www.geeksforgeeks.org/python-retain-records-with-n-occurrences-of-k/


def Retain(test_list, K, N):
    res = [ ele for ele in test_list if ele.count(K) == N]
    return res
if __name__ == "__main__":
    test_list = [(4, 5, 5, 4), (5, 4, 3)]
    K = 5
    N = 2
    result = Retain(test_list, K, N )
    print (result) 
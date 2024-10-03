#   https://www.geeksforgeeks.org/python-program-to-find-tuples-which-have-all-elements-divisible-by-k-from-a-list-of-tuples/

def Div(test_list, K ):
    res = [sub for sub in test_list if all(ele % K == 0 for ele in sub)]
    return res

if __name__ == "__main__":
    test_list = [(6, 24, 12), (7, 9, 6), (12, 18, 21)]
    K = 6 
    result = Div(test_list, K )
    print (result)

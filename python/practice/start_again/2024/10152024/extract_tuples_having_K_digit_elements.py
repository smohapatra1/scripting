#   https://www.geeksforgeeks.org/python-extract-tuples-having-k-digit-elements/

def Extract(test_list, K ):
    res = [ sub for sub in test_list if all(len(str(ele)) == K for ele in sub)]
    return res

if __name__ == "__main__":
    test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )]
    K = 2
    result = Extract(test_list, K )
    print (result)
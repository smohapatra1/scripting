#   https://www.geeksforgeeks.org/python-remove-tuples-of-length-k/

def Remove(test_list, K ):
    res = [ ele for ele in test_list if len(ele) != K ]
    return res

if __name__ == "__main__":
    test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
    K = 1 
    result = Remove(test_list, K )
    print (result)
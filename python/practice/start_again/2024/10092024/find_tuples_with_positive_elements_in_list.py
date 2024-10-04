#   https://www.geeksforgeeks.org/python-program-to-find-tuples-with-positive-elements-in-list-of-tuples/

def Positive(test_list):
    res = [ sub for sub in test_list if all(ele >= 0 for ele in sub)]
    return res

if __name__ == "__main__":
    test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, 6)]
    result = Positive(test_list)
    print (result)
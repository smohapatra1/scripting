#   https://www.geeksforgeeks.org/python-adding-tuple-to-list-and-vice-versa/

def Convert(test_list, test_tup):
    test_list +=test_tup
    return test_list

if __name__ == "__main__":
    test_list = [5, 6, 7]
    test_tup = [8,9,10]
    result = Convert(test_list, test_tup)
    print (result)
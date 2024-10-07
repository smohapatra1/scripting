#   https://www.geeksforgeeks.org/python-custom-sorting-in-list-of-tuples/

def Custom(test_list):
    res = sorted(test_list, key=lambda x : (-x[0], x[1]))
    return res

if __name__ == "__main__":
    test_list = [(7, 8), (5, 6), (7, 5), (10, 4), (10, 1)]
    result = Custom(test_list)
    print (result)
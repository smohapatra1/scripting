#   https://www.geeksforgeeks.org/python-filter-range-length-tuples/

def FilterRange(test_list):
    i, j = 2, 3
    res = [ sub for sub in test_list if len(sub) >= i and len(sub) <= j ]
    return res

if __name__ == "__main__":
    test_list = [(4, ), (5, 6), (2, 3, 5), (5, 6, 8, 2), (5, 9)]
 
    result = FilterRange(test_list)
    print (result)
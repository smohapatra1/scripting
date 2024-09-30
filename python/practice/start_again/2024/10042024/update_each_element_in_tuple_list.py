#   https://www.geeksforgeeks.org/python-update-each-element-in-tuple-list/

def Update(test_list):
    res = [tuple(j+ add_ele for j in sub) for sub in test_list]
    return res

if __name__ == "__main__":
    test_list = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
    add_ele = 4
    result = Update(test_list)
    print (result)
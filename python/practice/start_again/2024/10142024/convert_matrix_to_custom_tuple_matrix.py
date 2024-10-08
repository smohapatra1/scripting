#   https://www.geeksforgeeks.org/python-convert-matrix-to-custom-tuple-matrix/

def ConvertMatrix(test_list, add_list):
    res = [(ele1, ele2) for ele1, sub in zip(add_list, test_list) for ele2 in sub]
    return res

if __name__ == "__main__":
    test_list = [[4, 5, 6], [6, 7, 3], [1, 3, 4]]
    add_list = ['Gfg', 'is', 'best']
    result = ConvertMatrix(test_list, add_list)
    print (result)
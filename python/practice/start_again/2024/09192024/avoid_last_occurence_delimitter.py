#   https://www.geeksforgeeks.org/python-avoid-last-occurrence-of-delimitter/


def Delimitter(test_list, delim):
    res = delim.join(map(str, test_list))
    return res

if __name__ == "__main__":
    test_list = [4, 7, 8, 3, 2, 1, 9]
    delim = "$"
    result = Delimitter(test_list, delim)
    print (result)
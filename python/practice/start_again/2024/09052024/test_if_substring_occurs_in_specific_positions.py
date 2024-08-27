#   https://www.geeksforgeeks.org/python-test-if-substring-occurs-in-specific-position/

# https://www.geeksforgeeks.org/python-list-exercise/  - Main one 


def SpecificPosition(test_str, substr, i, j ):
    # Solution - 01 
    # res = test_str[i:j ] == substr
    # return res
    # Solution - 02 
    res = False 
    if (test_str.find(substr) == i):
        res = True
    return res

if __name__ == "__main__":
    test_str = "Gfg is best"
    substr = "best"
    i, j = 7, 11
    result = SpecificPosition(test_str, substr, i, j )
    print (result)
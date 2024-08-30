#   https://www.geeksforgeeks.org/python-uppercase-half-string/

def Upper(test_str):
    m = len(test_str)//2
    res = ''
    for i in range(len(test_str)):
        if i >= m:
            res +=test_str[i].upper()
        else:
            res +=test_str[i]
    return res

if __name__ == "__main__":
    # test_str = 'geeksforgeeks'
    test_str = 'apples'
    result = Upper(test_str)
    print (result)

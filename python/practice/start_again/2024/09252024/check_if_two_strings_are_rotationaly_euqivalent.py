#   https://www.geeksforgeeks.org/python-check-if-two-strings-are-rotationally-equivalent/

def equivalent(str1, str2):
    res = str2 in (str1 + str1)
    return res

if __name__ == "__main__":
    # str1 = 'GFG'
    # str2 = 'GGF'
    str1 = 'geeks'
    str2 = 'ksege'
    result = equivalent(str1, str2)
    print (result)
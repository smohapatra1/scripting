#   https://www.geeksforgeeks.org/python-string-till-substring/

def Till(test_string, spl_word):
    res = test_string.partition(spl_word)[0]
    return res

if __name__ == "__main__":
    test_string = "GeeksforGeeks is best for geeks"
    spl_word = 'best'
    result = Till(test_string, spl_word)
    print (result)
 
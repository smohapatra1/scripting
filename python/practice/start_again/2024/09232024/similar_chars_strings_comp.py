#   https://www.geeksforgeeks.org/python-similar-characters-strings-comparison/

def Compare(test_str1, test_str2):
    delim = ':'
    res = sorted(test_str1.split(':')) == sorted(test_str2.split(':'))
    return res

if __name__ == "__main__":
    test_str1 = 'e:e:k:s:g'
    test_str2 = 'g:e:e:k:s'
    result = Compare(test_str1, test_str2)
    print (result)
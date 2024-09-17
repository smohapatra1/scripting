#   https://www.geeksforgeeks.org/python-reverse-sort-a-string/

def Reverse(test_string):
    #   Solution - 01 
    # res = ''.join(sorted(test_string, reverse=True))
    # return res

    #   Solution - 02 
    temp = list(test_string)
    temp.sort(reverse=True)
    res = ''.join(temp)
    return res

if __name__ == "__main__":
    test_string = "geekforgeeks"
    result = Reverse(test_string)
    print (result)
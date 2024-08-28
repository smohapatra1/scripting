#   https://www.geeksforgeeks.org/reverse-words-given-string-python/

def Reverse(string):
    # Solution 1 
    # s = string.split()[::-1]
    # res = []
    # for i in s :
    #     res.append(i)
    # return ' '.join(res)

    # Solution 2 
    word = string.split(' ')
    res = ' '.join(reversed(word))
    return res


if __name__ == "__main__":
    string = "Samar is very good"
    result = Reverse(string)
    print (result)
#   https://www.geeksforgeeks.org/find-words-greater-given-length-k/


def Greater(str, k ):
    # Solution - 01 
    # s = str.split(' ')
    # res = []
    # # print (s)
    # for i in s :
    #     if len(i) > k:
    #         res.append(i)
    # return res
    # Solution - 02 
    
    return ([word for word in str.split(' ') if len(word) > k])

if __name__ == "__main__":
    k = 3
    str = "geek for geeks"
    result = Greater(str, k )
    print (result)
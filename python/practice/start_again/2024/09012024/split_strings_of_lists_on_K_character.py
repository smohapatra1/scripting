#   https://www.geeksforgeeks.org/python-split-string-of-list-on-k-character/?ref=leftbar-rightbar

# Using Join and Split 

def Split(test_list, K ):
    res = K.join(test_list).split(K)
    return res 


if __name__ == "__main__":
    test_list = ['Gfg is best', 'for Geeks', 'Preparing']
    K = ' '
    result = Split(test_list, K )
    print (result)
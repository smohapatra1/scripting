#   https://www.geeksforgeeks.org/python-list-product-excluding-duplicates/

import math
def product (list):
    # SOlution - 1 

    # s = set(list)
    # return (math.prod(s))
    
    #Solution - 2
    s = set(l)
    res = 1 
    for i in s:
        res = res * i
    return res
l = [1, 3, 5, 6, 3, 5, 6, 1,8]
print (product(l))
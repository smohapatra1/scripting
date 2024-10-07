#   https://www.geeksforgeeks.org/python-program-to-covert-tuple-into-list-by-adding-the-given-string-after-every-element/

def Add(test_tup, K ):
    res = [ ele for sub in test_tup for ele in (sub, K )]
    return res 

if __name__ == "__main__":
    test_tup = (5, 6, 7, 4, 9)
    K = 'Gfg'
    result = Add(test_tup, K)
    print (result) 
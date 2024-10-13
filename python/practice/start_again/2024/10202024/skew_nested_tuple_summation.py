#   https://www.geeksforgeeks.org/python-skew-nested-tuple-summation/

def SkewSum(test_tup):
    print ("Current List : " + str(test_tup))
    res = 0
    while test_tup:
        res +=test_tup[0]
        test_tup = test_tup[1]
    return res

if __name__ == "__main__":
    test_tup = (5, (6, (1, (9, (10, None)))))
    print ("Result After Summation = ", SkewSum(test_tup))
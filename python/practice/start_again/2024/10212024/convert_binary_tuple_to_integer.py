#   https://www.geeksforgeeks.org/python-convert-binary-tuple-to-integer/

def BinToIntTup(test_tup):
    print ("Current Tuple : " + str(test_tup))
    res = int("".join(str(ele) for ele in test_tup), 2 )
    return res
if __name__ == "__main__":
    test_tup = (1, 1, 0, 1, 0, 0, 1)
    print ("Final conversion from Binary to Tuple ",BinToIntTup(test_tup) )
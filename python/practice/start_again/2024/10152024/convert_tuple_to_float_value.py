#   https://www.geeksforgeeks.org/python-convert-tuple-to-float-value/

def TupleToFloat(test_tup):
    res = float('.'.join(str(ele) for ele in test_tup))
    return res

if __name__ == "__main__":
    test_tup = (4, 56) 
    result = TupleToFloat(test_tup)
    print (result)
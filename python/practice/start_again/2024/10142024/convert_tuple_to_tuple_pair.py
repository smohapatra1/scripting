#   https://www.geeksforgeeks.org/python-convert-tuple-to-tuple-pair/

def Pair(test_tuple):
    res = tuple(zip(test_tuple[:-1], test_tuple[1:]))
    return res
if __name__ == "__main__":
    test_tuple = ('G', 'F', 'G')
    result = Pair(test_tuple)
    print (result)
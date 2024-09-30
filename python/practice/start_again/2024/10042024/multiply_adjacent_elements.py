#   https://www.geeksforgeeks.org/python-multiply-adjacent-elements/

def Multiply(test_tup):
    res = tuple(i * j for i, j in zip(test_tup, test_tup[1:]))
    return res
if __name__ == "__main__":
    test_tup = (1, 5, 7, 8, 10)
    result = Multiply(test_tup)
    print (result)
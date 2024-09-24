#   https://www.geeksforgeeks.org/python-split-by-repeating-substring/

def Split(test_str, K ):
    temp = len(test_str)// len(K)
    res = [K] * temp
    return res

if __name__ == "__main__":
    test_str = "gfggfggfggfggfggfggfggfg"
    K = 'gfg'
    result = Split(test_str, K )
    print (result)
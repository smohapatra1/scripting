#   https://www.geeksforgeeks.org/python-remove-keys-with-values-greater-than-k-including-mixed-values/

def Remove(test_dict, K ):
    res = {}
    for key in test_dict:
        if not (isinstance(test_dict[key], int) and test_dict[key]> K ):
            res[key] = test_dict[key]
    return res

if __name__ == "__main__":
    test_dict = {'Gfg' : 3, 'is' : 7, 'best' : 10, 'for' : 6, 'geeks' : 'CS'} 
    K = 6 
    print ("Results after removed the values > %d ", (Remove(test_dict, K )), K )
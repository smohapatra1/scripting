#   https://www.geeksforgeeks.org/python-dictionary-values-mean/

def Mean(test_dict):
    res = 0 
    for val in test_dict.values():
        res +=val
    return res/len(test_dict)

if __name__ == "__main__":
    test_dict = {"Gfg" : 4, "is" : 7, "Best" : 8, "for" : 6, "Geeks" : 10} 
    print ("Mean values are : ", Mean(test_dict))
#   https://www.geeksforgeeks.org/python-filter-dictionary-values-in-heterogeneous-dictionary/

def Heterogeneous(test_dict, K ):
    res = {key : val for key, val in test_dict.items() if type(val) !=int or val > K }
    return res
if __name__ == "__main__":
    test_dict = {'Gfg' : 4, 'is' : 2, 'best' : 3, 'for' : 'geeks'}
    K = 3 
    print ("Values greater than K : ", Heterogeneous(test_dict, K ))
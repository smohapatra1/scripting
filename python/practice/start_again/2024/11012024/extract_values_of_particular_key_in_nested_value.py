#   https://www.geeksforgeeks.org/python-extract-values-of-particular-key-in-nested-values/

def Extract(test_dict):
    temp = 'c'
    res = [val[temp] for key, val in test_dict.items() if temp in val]
    return res
if __name__ == "__main__":
    test_dict = {'Gfg' : {"a" : 7, "b" : 9, "c" : 12},
             'is' : {"a" : 15, "b" : 19, "c" : 20}, 
             'best' :{"a" : 5, "b" : 10, "c" : 2}}
    print ("Values after extracting them : ", Extract(test_dict))
#   https://www.geeksforgeeks.org/python-dictionary-with-maximum-count-of-pairs/

def MaxList(test_list):
    # Solution -01 
    # res = max(test_list, key= len)
    # return res
    # Solution - 02 
    res = {}
    Max_Len = 0 
    for val in test_list:
        if len(val) > Max_Len:
            res = val
            Max_Len = len(val)
    return res

if __name__ == "__main__":
    test_list = [{"gfg": 2, "best" : 4},  
             {"gfg": 2, "is" : 3, "best" : 4},  
             {"gfg": 2}] 
    print ("Max len of lists are : ", MaxList(test_list))
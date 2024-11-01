#   https://www.geeksforgeeks.org/python-sort-dictionaries-list-by-keys-value-list-index/

def Sort(test_list, K ):
    idx = 2 
    res = sorted(test_list, key=lambda ele:ele[K][idx])
    return res

if __name__ == "__main__":
    test_list = [{"Gfg" : [6, 7, 8], "is" : 9, "best" : 10}, 
             {"Gfg" : [2, 0, 3], "is" : 11, "best" : 19},
             {"Gfg" : [4, 6, 9], "is" : 16, "best" : 1}]
    K = 'Gfg'
    print ("Results after sorting: ", Sort(test_list, K ))
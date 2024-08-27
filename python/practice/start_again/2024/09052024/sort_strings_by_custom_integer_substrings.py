#   https://www.geeksforgeeks.org/python-sort-string-by-custom-integer-substrings/

import re
def SortString(test_list, subord_list):
    res = {val : key for key, val in enumerate(subord_list)}
    res_list = sorted([[ele, res [re.search("(\d+)$", ele ).group()]] for ele in test_list], key = lambda x:x[1])
    res1 = [ ele for ele in list(zip(*res_list))[0]] 
    return res1





if __name__ == "__main__":
    test_list = ["Good at 4", "Wake at 7", "Work till 6", "Sleep at 11"]
    subord_list = ["6", "7", "4", "11"]
    result = SortString(test_list, subord_list)
    print (result)
#   https://www.geeksforgeeks.org/python-add-space-between-potential-words/

#   Using regex 
#   Using isupper and replace 

import re

def AddSpace(test_list):
    # Solution - 01 
    # res = [re.sub(r"(\w)([A-Z])", r"\1 \2", ele ) for ele in test_list]
    # return res
    # Solution - 02 
    res = []
    for i in test_list:
        for j in i:
            if (j.isupper()):
                i = i.replace(j, ' '+j)
        res.append(i)
    return res

if __name__ == "__main__":
    test_list = ["gfgBest", "forGeeks", "andComputerScience"]
    result = AddSpace(test_list)
    print (result)
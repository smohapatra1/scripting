#   https://www.geeksforgeeks.org/python-convert-nested-dictionary-to-mapped-tuple/
from collections import defaultdict

def NestedDictToTuple(test_dict):
    res = defaultdict(tuple)
    for key, val in test_dict.items():
        for ele in val:
            res[ele] += (val[ele], )
    return res
if __name__ == "__main__":
    test_dict = {'gfg' : {'x' : 5, 'y' : 6}, 
                'is' : {'x' : 1, 'y' : 4},
                'best' : {'x' : 8, 'y' : 3}}
    print ("Final list ", NestedDictToTuple(test_dict))
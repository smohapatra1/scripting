#   https://www.geeksforgeeks.org/python-swapping-hierarchy-in-nested-dictionaries/

from collections import defaultdict

def Swap(test_dict):
    res = defaultdict(dict)
    for key, val in test_dict.items():
        for key_in, val_in in val.items():
            res[key_in][key] = val_in
    return dict(res)

if __name__ == "__main__":
    test_dict = {'Gfg': { 'a' : [1, 3], 'b' : [3, 6], 'c' : [6, 7, 8]},
             'Best': { 'a' : [7, 9], 'b' : [5, 3, 2], 'd' : [0, 1, 0]}}
    print ("Result after swapping : ", Swap(test_dict))
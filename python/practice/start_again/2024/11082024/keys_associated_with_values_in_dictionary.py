#   https://www.geeksforgeeks.org/python-keys-associated-with-values-in-dictionary/?ref=leftbar-rightbar
from collections import defaultdict

def Association(test_dict):
    res = defaultdict(list)
    for key, val in test_dict.items():
        for ele in val:
            res[ele].append(key)
    return dict(res)

if __name__ == "__main__":
    test_dict = {'gfg' : [1, 2, 3], 'is' : [1, 4], 'best' : [4, 2]}
    print ("Results after association: ", Association(test_dict))
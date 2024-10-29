#   https://www.geeksforgeeks.org/python-extract-unique-values-dictionary-values/?ref=leftbar-rightbar

def Unique(test_dict):
    res = list(sorted({ele for val in test_dict.values() for ele in val}))
    return res

if __name__ == "__main__":
    test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}
    print ("Results after sorting : ", Unique(test_dict))
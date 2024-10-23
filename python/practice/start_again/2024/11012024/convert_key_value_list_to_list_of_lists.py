#   https://www.geeksforgeeks.org/python-convert-key-value-list-dictionary-to-list-of-lists/?ref=leftbar-rightbar

def DictList(test_dict):
    # Solution - 01 
    # res = []
    # for key, val in test_dict.items():
    #     res.append([key] + val)
    # return res
    # Solution - 02 
    res = [[key] + val for key, val in test_dict.items()]
    return res

if __name__ == "__main__":
    test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
    print ("Results after converting from Dict to List : ", DictList(test_dict))
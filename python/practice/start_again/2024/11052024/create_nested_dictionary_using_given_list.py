#   https://www.geeksforgeeks.org/python-create-nested-dictionary-using-given-list/

def NestedList(test_dict, test_list):
    # Solution - 01 
    # res = {}
    # for key, val in zip(test_list, test_dict.items()):
    #     res[key] = dict([val])
    # return res
    # Solution - 02 
    res = {idx: {key: test_dict[key]} for idx, key in zip(test_list, test_dict)}
    return res

if __name__ == "__main__":
    test_dict = {'Gfg' : 4, 'is' : 5, 'best' : 9} 
    test_list = [8, 3, 2]
    print ("Result after combining ", NestedList(test_dict, test_list))
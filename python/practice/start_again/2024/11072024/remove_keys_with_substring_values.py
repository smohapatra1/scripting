#   https://www.geeksforgeeks.org/python-remove-keys-with-substring-values/

def RemoveKeys(test_dict, sub_list):
    # Solution - 01 
    # res = {}
    # for key, val in test_dict.items():
    #     if not any(ele in val for ele in sub_list):
    #         res[key] = val
    # return res
    # Solution - 02 
    res1 = {key: val for key, val in test_dict.items() if not any(ele in val for ele in sub_list)}
    return res1

if __name__ == "__main__":
    test_dict = {1 : 'Gfg is best for geeks', 2 : 'Gfg is good', 3 : 'I love Gfg'}
    # printing original dictionary
    print("The original dictionary : ",  test_dict)
    # initializing substrings
    sub_list = ['love', 'good']
    print ("Results after removing keys : ", RemoveKeys(test_dict, sub_list))
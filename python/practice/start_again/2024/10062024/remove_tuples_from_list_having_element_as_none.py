#   https://www.geeksforgeeks.org/python-remove-tuples-from-the-list-having-every-element-as-none/

def RemoveTuples(test_list):
    # Solution - 01 
    # res = []
    # for i in test_list:
    #     if not (i.count(None) == len(i)):
    #         res.append(i)
    # return res

    # Solution - 02 
    res = [sub for sub in test_list if not all (ele == None for ele in sub) ]
    return res



if __name__ == "__main__":
    test_list = [(None, 2), (None, None), (3, 4), (12, 3), (None, )]
    result = RemoveTuples(test_list)
    print (result)
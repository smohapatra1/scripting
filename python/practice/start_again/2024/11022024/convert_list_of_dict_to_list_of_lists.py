#   https://www.geeksforgeeks.org/python-convert-list-of-dictionaries-to-list-of-lists/?ref=leftbar-rightbar

def DictToLists(test_list):

    # Solution -01 
    # res = [[key for key in test_list[0].keys()] , *[list(idx.values()) for idx in test_list]]
    # return res
    # Solution - 02 
    res = []
    for idx, val in enumerate(test_list, start=0):
        if idx == 0:
            res.append(list(val.keys()))
            res.append(list(val.values()))
        else:
            res.append(list(val.values()))
    return res

if __name__ == "__main__":
    test_list = [{'Nikhil' : 17, 'Akash' : 18, 'Akshat' : 20},
             {'Nikhil' : 21, 'Akash' : 30, 'Akshat' : 10},
             {'Nikhil' : 31, 'Akash' : 12, 'Akshat' : 19}]
    print ("Result after converting: ", DictToLists(test_list))
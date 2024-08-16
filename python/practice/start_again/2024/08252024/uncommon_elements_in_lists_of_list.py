#   https://www.geeksforgeeks.org/python-uncommon-elements-in-lists-of-list/?ref=leftbar-rightbar

def UncommonList(test_list1, test_list2):
    # Solution - 1 
    res = []
    for i in test_list1:
        if i not in test_list2:
            res.append(i)
    for i in test_list2:
        if i not in test_list1:
            res.append(i)
    return res
    # Solution - 2 
    # res_set = set(map(tuple, test_list1)) ^ set(map(tuple, test_list2))
    # print (res_set)
    # res_list = list(map(list, res_set))
    # print ("The uncommon of two lists is : " + str(res_list))


if __name__ == "__main__":
    test_list1 = [ [1, 2], [3, 4], [5, 6] ]
    test_list2 = [ [3, 4], [5, 7], [1, 2] ]
    result = UncommonList(test_list1, test_list2)
    print (result)
#   https://www.geeksforgeeks.org/python-filter-the-list-of-string-whose-index-in-second-list-contaons-the-given-substring/

def FilterString(test_list1, test_list2, sub_str):
    # Solution - 01 
    # res = []
    # for ele1, ele2 in zip(test_list1, test_list2):
    #     if sub_str in ele2:
    #         res.append(ele1)
    # Solution - 02 
    print("The original list 1 is : " + str(test_list1))
    print("The original list 2 is : " + str(test_list2))
    res = [ ele1 for ele1, ele2 in zip(test_list1, test_list2) if sub_str in ele2]
    return res

if __name__ == "__main_":
    test_list1 = ["Gfg", "is", "not", "best", "and","not", "for", "CS"]
    test_list2 = ["Its ok", "all ok", "wrong", "looks ok", "ok", "wrong", "ok", "thats ok"]
    sub_str = "ok"
    result = FilterString(test_list1, test_list2, sub_str)
    print (result)
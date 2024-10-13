#   https://www.geeksforgeeks.org/python-intersection-in-tuple-records-data/

def Intersections(test_list1, test_list2):
    res = [ ele1 for ele1 in test_list1 for ele2 in test_list2 if ele1 == ele2]
    return res
if __name__ == "__main__":
    test_list1 = [('gfg', 1), ('is', 2), ('best', 3)]
    test_list2 = [('i', 3), ('love', 4), ('gfg', 1)]
    result = Intersections(test_list1, test_list2)
    print (result)
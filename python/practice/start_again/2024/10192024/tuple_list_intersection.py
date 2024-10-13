#   https://www.geeksforgeeks.org/python-tuple-list-intersection-order-irrespective/

def Intersections(test_list1, test_list2):
    res = set([tuple(sorted(ele)) for ele in test_list1]) & set([tuple(sorted(ele)) for ele in test_list2])
    return res

if __name__ == "__main__":
    test_list1 = [(3, 4), (5, 6), (9, 10), (4, 5)]
    test_list2 = [(5, 4), (3, 4), (6, 5), (9, 11)]
    result = Intersections(test_list1, test_list2)
    print (result)

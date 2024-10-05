#   https://www.geeksforgeeks.org/python-cross-pairing-in-tuple-list/

def CrossPairing(test_list1, test_list2):
    res = [(a[1], b[1]) for a,b in zip(test_list1, test_list2) if a[0] == b[0]]
    return res

if __name__ == "__main__":
    test_list1 = [(1, 7), (6, 7), (9, 100), (4, 21)]
    test_list2 = [(1, 3), (2, 1), (9, 7), (2, 17)]
    result = CrossPairing(test_list1, test_list2)
    print ("Final List after cross pairing in tuple = " +str(result))
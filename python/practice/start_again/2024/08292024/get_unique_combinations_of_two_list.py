#   https://www.geeksforgeeks.org/python-program-to-get-all-unique-combinations-of-two-lists/

def UniqueCombinations(list1, list2):
    res = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            res.append((list1[i], list2[j]))
    return res

if __name__ == "__main__":
    list1 = [ "a", "b", "c", "d", "e" ]
    list2 = [ 2, 9, 8, 6, 5 ]
    result = UniqueCombinations(list1, list2)
    print (result)

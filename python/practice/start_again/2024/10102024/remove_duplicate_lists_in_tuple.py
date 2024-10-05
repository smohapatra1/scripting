#   https://www.geeksforgeeks.org/python-remove-duplicate-lists-in-tuples-preserving-order/

def RemDuplicate(test_tup):
    print ("Current Tuple : " + str(test_tup))
    temp = set()
    res = [ ele for ele in test_tup if not (tuple(ele) in temp or temp.add(tuple(ele)))]
    return res

if __name__ == "__main__":
    test_tup = ([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])
    result = RemDuplicate(test_tup)
    print ("After removing duplicates : " + str(result))
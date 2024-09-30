#   https://www.geeksforgeeks.org/python-all-pair-combinations-of-2-tuples/

def AllPair(test_tuple1, test_tuple2):
    res = [(a,b )for a in test_tuple1 for b in test_tuple2]
    res = res + [(a,b) for a in test_tuple2 for b in test_tuple1]
    return res

if __name__ == "__main__":
    test_tuple1 = (4, 5)
    test_tuple2 = (7, 8)
    result = AllPair(test_tuple1, test_tuple2)
    print (result)

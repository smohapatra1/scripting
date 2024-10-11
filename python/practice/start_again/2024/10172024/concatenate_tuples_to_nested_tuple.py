#   https://www.geeksforgeeks.org/python-how-to-concatenate-tuples-to-nested-tuples/

def Concatenate(test_tup1, test_tup2):
    res = test_tup1 + test_tup2
    return res

if __name__ == "__main__":
    test_tup1 = (3, 4),
    test_tup2 = (5, 6),
    print("Results After concatenate : ", Concatenate(test_tup1, test_tup2))
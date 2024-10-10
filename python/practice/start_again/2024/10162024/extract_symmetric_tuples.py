#   https://www.geeksforgeeks.org/python-extract-symmetric-tuples/

def ExtractSymmetric(test_list):
    temp = set(test_list) & {(b,a) for a,b in test_list }
    res = {(a,b) for a,b in temp if a <b}
    return res

if __name__ == "__main__":
    test_list = [(6, 7), (2, 3), (7, 6), (9, 8), (10, 2), (8, 9)]
    result = ExtractSymmetric(test_list)
    print (result)
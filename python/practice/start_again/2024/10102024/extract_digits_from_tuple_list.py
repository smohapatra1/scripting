#   https://www.geeksforgeeks.org/python-extract-digits-from-tuple-list/
def Extract(test_list):
    res = ""
    for i in test_list:
        for j in i:
            res+=str(j)
    res = list(map(int, set(res)))
    return res

if __name__ == "__main__":
    test_list = [(15, 3), (3, 9), (1, 10), (99, 2)]
    result = Extract(test_list)
    print (result)

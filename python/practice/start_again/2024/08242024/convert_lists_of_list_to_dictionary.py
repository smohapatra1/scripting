#   https://www.geeksforgeeks.org/python-convert-lists-of-list-to-dictionary/

def listListDict(test_list):
    res = dict()
    for i in test_list:
        res[tuple(i[:2])] = tuple(i[2:])
    return res
if __name__ == "__main__":
    test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
    r = listListDict(test_list)
    print (r)
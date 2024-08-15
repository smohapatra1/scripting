#   https://www.geeksforgeeks.org/python-convert-list-to-list-of-dictionaries/

def ListDict(test_list):
    n = len(test_list)
    res = []
    key_list=["name", "number"]
    for i in range(0, n, 2):
        res.append({key_list[0]: test_list[i], key_list[1]: test_list[i+1]})
    return res

if __name__ == "__main__":
    test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]
    result = ListDict(test_list)
    print (result)
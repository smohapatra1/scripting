#   https://www.geeksforgeeks.org/python-remove-redundant-substrings-from-strings-list/

def RemoveSub(test_list):
    test_list.sort(key = len)
    res = []
    for idx, val  in enumerate(test_list):
        if val not in ', '.join(test_list[idx + 1:]):
            res.append(val)
    return res
if __name__ == "__main__":
    test_list = ["Gfg", "Gfg is best", "Geeks", "Gfg is for Geeks"]
    res = RemoveSub(test_list)
    print (res)

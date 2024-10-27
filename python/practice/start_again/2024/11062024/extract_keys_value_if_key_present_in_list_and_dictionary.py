#   https://www.geeksforgeeks.org/python-extract-keys-value-if-key-present-in-list-and-dictionary/

def Extract(test_dict, test_list, K ):
    res = None
    if all (K in sub for sub in [test_dict, test_list]):
        res = test_dict[K]
    return res


if __name__ == "__main__":
    test_list = ["Gfg", "is", "Good", "for", "Geeks"]
    # initializing Dictionary
    test_dict = {"Gfg" : 2, "is" : 4, "Best" : 6}
    K = 'Gfg'
    print ("Results after extracting keys ", Extract(test_dict, test_list, K ))
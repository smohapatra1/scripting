#   https://www.geeksforgeeks.org/python-replace-words-from-dictionary/

def Replace(test_str, lookup_dict):
    res = " ".join(lookup_dict.get(ele, ele) for ele in test_str.split())
    return res

if __name__ == "__main__":
    test_str = 'geekforgeeks best for geeks'
    lookup_dict = {"best" : "good and better", "geeks" : "all CS aspirants"}
    print ("Complete word after replacing new words :", Replace(test_str, lookup_dict))
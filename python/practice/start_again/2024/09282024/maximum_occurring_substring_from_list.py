#   https://www.geeksforgeeks.org/python-maximum-occurring-substring-from-list/

def MaxOccurr( test_list, test_str):
    res = []
    for i in test_list:
        res.append(test_str.count(i))
    x = max(res)
    out = test_list[res.index(x)]
    return out

if __name__ == "__main__":
    test_str = "gfghsisbjknlmkesbestgfgsdcngfgcsdjnisdjnlbestdjsklgfgcdsbestbnjdsgfgdbhisbhsbestdkgfgb"
    test_list = ['gfg', 'is', 'best']
    result = MaxOccurr(test_list, test_str)
    print (result)
#   https://www.geeksforgeeks.org/python-extract-indices-of-substring-matches/

def ExtractIndexes(test_list, K ):
    res = []
    for idx, ele in enumerate(test_list):
        if K in ele:
            res.append(idx)
    return res

if __name__ == "__main__":
    test_list = ["Gfg is good", "for Geeks", "I love Gfg", "Its useful"]
    # initializing K 
    K = "Gfg"
    result = ExtractIndexes( test_list, K)
    print (result)
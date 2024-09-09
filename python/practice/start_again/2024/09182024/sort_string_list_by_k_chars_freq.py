#   https://www.geeksforgeeks.org/python-sort-string-list-by-k-character-frequency/

def Sort(test_list, K ):
    res = sorted(test_list, key = lambda ele:-ele.count(K))
    return res

if __name__ == "__main__":
    test_list = ["geekforgeeks", "is", "best", "for", "geeks"]
    K = 'e'
    result = Sort(test_list, K )
    print (result)

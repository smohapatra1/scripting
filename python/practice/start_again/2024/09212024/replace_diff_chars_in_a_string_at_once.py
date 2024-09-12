#   https://www.geeksforgeeks.org/python-replace-different-characters-in-string-at-once/

def DiffChar(test_str):
    map_dict = {'e': '1', 'b': '6', 'i': '4'}
    res = ''.join(idx if idx not in map_dict else map_dict[idx] for idx in test_str)
    return res

if __name__ == "__main__":
    test_str = 'geeksforgeeks is best'
    result = DiffChar(test_str)
    print (result)
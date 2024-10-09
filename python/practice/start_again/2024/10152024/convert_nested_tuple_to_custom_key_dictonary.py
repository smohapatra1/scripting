#   https://www.geeksforgeeks.org/python-convert-nested-tuple-to-custom-key-dictionary/

def nestedTuple(test_tuple):
    res = [{'key': sub[0], 'value': sub[1], 'id' : sub[2]} for sub in test_tuple]
    return res

if __name__ == "__main__":
    test_tuple = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))
    result = nestedTuple(test_tuple)
    print (result)
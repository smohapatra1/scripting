#   https://www.geeksforgeeks.org/python-convert-list-of-lists-to-tuple-of-tuples/

def ConvertList(test_list):
    res = tuple(tuple(sub) for sub in test_list)
    return res

if __name__ == "__main__":
    test_list = [['Gfg', 'is', 'Best'], ['Gfg', 'is', 'love'],['Gfg', 'is', 'for', 'Geeks']]
    result = ConvertList(test_list)
    print (result)
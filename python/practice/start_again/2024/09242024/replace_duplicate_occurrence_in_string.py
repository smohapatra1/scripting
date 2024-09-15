#   https://www.geeksforgeeks.org/python-replace-duplicate-occurrence-in-string/?ref=leftbar-rightbar

def DupOcc(test_str):
    test_list = test_str.split(' ')
    res = ' '.join([repl_dict.get(val) if val in repl_dict.keys() and test_list.index(val) != idx else val for idx, val in enumerate(test_list)])
    return res


if __name__ == "__main__":
    test_str = 'Gfg is best . Gfg also has Classes now. Classes help understand better . '
    repl_dict = {'Gfg' : 'It', 'Classes' : 'They'}
    result = DupOcc(test_str)
    print (result)
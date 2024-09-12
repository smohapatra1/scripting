#   https://www.geeksforgeeks.org/python-mirror-image-of-string/

def Mirror(test_str):
    mir_dict = {'b': 'd', 'd': 'b', 'i': 'i', 'o': 'o', 'v': 'v', 'w': 'w', 'x': 'x'}
    res = test_str[::-1]
    res_1 = ''
    for ele in res:
        if ele in mir_dict:
            res_1  +=mir_dict[ele]
        else:
            res = 'Not possible '
            break
    mir_str = res_1[::-1]
    return mir_str
    
if __name__ == "__main__":
    test_str = 'void'
    result = Mirror(test_str)
    print (result)
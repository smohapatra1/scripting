#   https://www.geeksforgeeks.org/python-convert-key-values-list-to-flat-dictionary/?ref=leftbar-rightbar

def FlatDict(test_dict):
    res = dict(zip(test_dict['month'], test_dict['name']))
    return res

if __name__ == "__main__":
    test_dict = {'month' : [1, 2, 3], 'name' : ['Jan', 'Feb', 'March']}
    print ("Results after converting : ", FlatDict(test_dict))
#   https://www.geeksforgeeks.org/python-flatten-tuples-list-to-string/
from itertools import chain

def Flatten(test_list):
    # Solution - 01 
    # res = []
    # for i in test_list:
    #     res.extend(list(i))
    # res = ' '.join(res)
    # return res

    # Solution - 02 
    res = ' '.join(chain(*test_list))
    return res

if __name__ == "__main__":
    test_list = [('1', '4', '6'), ('5', '8'), ('2', '9'), ('1', '10')]
    result = Flatten(test_list)
    print (result)
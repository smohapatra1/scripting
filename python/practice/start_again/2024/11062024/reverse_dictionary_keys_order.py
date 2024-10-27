#   https://www.geeksforgeeks.org/python-reverse-dictionary-keys-order/
from collections import OrderedDict

def Reverse(test_dict):
    print ("Original Dictionary : ",  test_dict)
    res = OrderedDict(reversed(test_dict.items()))
    return res

if __name__ == "__main__":
    test_dict = {'gfg' : 4, 'is' : 2, 'best' : 5}
    print ("Reversing the dictionaries are : ", Reverse(test_dict))
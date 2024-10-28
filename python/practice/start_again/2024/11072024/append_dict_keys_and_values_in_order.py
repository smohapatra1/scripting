#   https://www.geeksforgeeks.org/python-append-dictionary-keys-and-values-in-order-in-dictionary/?ref=leftbar-rightbar

from itertools import chain
def Append(test_dict):
    # Solution -01 
    # res = list(chain(test_dict.keys(), test_dict.values()))
    # return res
    res = list(test_dict.keys()) + list(test_dict.values())
    return res

if __name__ == "__main__":
    test_dict = {"Gfg" : 1, "is" :  3, "Best" : 2}
    print ("Results after appending kays and values : ", Append(test_dict))
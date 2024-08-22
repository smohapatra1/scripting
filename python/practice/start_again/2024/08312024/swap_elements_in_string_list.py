#   https://www.geeksforgeeks.org/python-swap-elements-in-string-list/


def Swap(test_list):
    res = [ sub.replace('G', '-').replace('e', 'G').replace('o', 'a') for sub in test_list]
    return res
if __name__ == "__main__":
    test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']
    result = Swap(test_list)
    print (result)
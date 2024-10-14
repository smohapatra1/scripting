# https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/
from collections import OrderedDict

def SortedD(d):

    print ("Current Dictionary    : " + str(d))
    # Solution - 01 
    # myKeys = list(d.keys())
    # myKeys.sort()
    # sd = {i: d[i] for i in myKeys}
    # return sd
    # Solution - 02 
    d1 = OrderedDict(sorted(d.items()))
    return d1

if __name__ == "__main__":
    # d = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15}
    d = {2: 56, 1: 2, 5: 12, 4: 24}
    print ("Results after sorting : ", SortedD(d))
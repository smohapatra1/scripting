#   https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/
from collections import OrderedDict

def Sort(d):
    d1 = OrderedDict(sorted(d.items()))
    return d1

if __name__ == "__main__":
    d = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15}
    print ("Before sorted : ", d)
    print ("After Sorted : ", Sort(d))
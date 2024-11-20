#   https://www.geeksforgeeks.org/problems/remove-all-duplicates-from-a-given-string4321/1

from collections import OrderedDict

def RemoveDup(s):
    # return ''.join(set(s))
    return ''.join(OrderedDict.fromkeys(s))


if __name__ == "__main__":
    s = "geEksforGEeks"
    print ("Current String ", s)
    print ("After removing Duplicate ", RemoveDup(s))
#   https://www.geeksforgeeks.org/remove-duplicates-given-string-python/

from collections import OrderedDict
def removeDupWithout(str):
    return "".join(set(str))

def WithOrder(str):
    return "".join(OrderedDict.fromkeys(str))

if __name__ == "__main__":
    str = "geeksforgeeks"
    print ("Without Order= ", removeDupWithout(str))
    print ("With Order   = ", WithOrder(str))
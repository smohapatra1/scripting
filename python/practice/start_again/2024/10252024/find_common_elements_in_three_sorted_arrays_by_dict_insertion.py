#   https://www.geeksforgeeks.org/python-dictionary-intersection-find-common-elements-three-sorted-arrays/

from collections import OrderedDict
def CommonElements(ar1, ar2, ar3):
    list = []
    dict1 = OrderedDict.fromkeys(ar1)
    dict2 = OrderedDict.fromkeys(ar2)
    dict3 = OrderedDict.fromkeys(ar3)
    for values1, keys1 in dict1.items():
        for values2, keys2 in dict2.items():
            for values3, key3 in dict3.items():
                if values1 == values2 == values3:
                    list.append(values1)
    return list
if __name__ == "__main__":
    ar1 = [1, 5, 10, 20, 40, 80]
    ar2 = [6, 7, 20, 80, 100]
    ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
    print ("Common Elements are : ", CommonElements(ar1, ar2, ar3))
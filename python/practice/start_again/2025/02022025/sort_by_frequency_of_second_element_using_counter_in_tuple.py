#   https://www.geeksforgeeks.org/python-sort-by-frequency-of-second-element-in-tuple-list/?ref=ml_lbp

from collections import Counter
def SecondList(test_list):
    freq = Counter(val for key,val in test_list)
    res = sorted(test_list, key=lambda ele: freq[ele[1]], reverse=True)
    return res

if __name__ == "__main__":
    test_list = [(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]
    print ("Original list :", test_list)
    print ("Sorted List   :", SecondList(test_list))

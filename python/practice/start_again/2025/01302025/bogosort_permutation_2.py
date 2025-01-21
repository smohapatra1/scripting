#   https://www.geeksforgeeks.org/python-program-for-bogosort-or-permutation-sort/

import random

def bogoSort(a):
    n = len(a)
    while not sorted(a) == a:
        random.shuffle(a)


if __name__ == "__main__":
    a = [3, 2, 4, 1, 0, 5]
    print ("Unsorted Array : ", a)
    bogoSort(a)
    print ("Sorted Array   : ", a)
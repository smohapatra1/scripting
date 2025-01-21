#   https://www.geeksforgeeks.org/python-program-for-bogosort-or-permutation-sort/

import random

def bogoSort(a):
    while (is_sorted(a) == False):
        shuffle(a)
def is_sorted(a):
    for i in range(0, n-1):
        if a[i] > a[i+1]:
            return False
    return True
def shuffle(a):
    for i in range(0, n ):
        r = random.randint(0, n-1)
        a[i], a[r] = a[r], a[i]

if __name__ == "__main__":
    a = [3, 2, 4, 1, 0, 5]
    n = len(a)
    print ("Unsorted Array : ", a)
    bogoSort(a)
    print ("Sorted Array   : ", a )

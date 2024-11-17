#   https://www.geeksforgeeks.org/problems/intersection-of-two-sorted-array-1587115620/1
import numpy as np

def Intersection(a,b):
    # Solution - 01 
    # print ([x for x in set(a) & set(b)])
    # Solution - 02 
    a1 = np.array(a)
    b1 = np.array(b)
    print (np.intersect1d(a1, b1 ))

if __name__ == "__main__":
    a = [ 10, 11, 12, 14, 15, 20]
    b = [ 20, 21, 22, 23, 25, 26]
    Intersection(a,b)
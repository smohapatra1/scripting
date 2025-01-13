#   https://www.geeksforgeeks.org/python-program-for-binary-search/

import bisect

def binary_search_bisect(arr, x ):
    res = bisect.bisect_left(arr, x)
    if res != len(arr) and arr[res] == x:
        return res
    else:
        return -1

if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    # Function call
    result = binary_search_bisect(arr, x)
    if result != -1 :
        print ("Element is present at Index ", result )
    else:
        print ("Element not present in the Array")
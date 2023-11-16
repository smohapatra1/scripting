# #   https://leetcode.com/problems/find-k-closest-elements/

# 658. Find K Closest Elements
# Medium
# 7.7K
# 614
# Companies
# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
 

# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:

# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]

from typing import List
def ClosestElement( arr: List[int], k: int, x: int) -> List[int]:
    low =0 
    high = len(arr) -k 
    while low < high:
        mid = ( low + high )//2
        if x - arr[mid]  > arr[mid+k] -x:
            low = mid + 1
        else:
            high = mid
    return arr[low: low+k ]


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    k = 4
    x = 3
    print ("{}".format(ClosestElement(arr, k, x )))


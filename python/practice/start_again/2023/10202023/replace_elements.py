# #   https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

# 1299. Replace Elements with Greatest Element on Right Side
# Easy
# 2.4K
# 232
# Companies
# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

# After doing so, return the array.

 

# Example 1:

# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation: 
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.
# Example 2:

# Input: arr = [400]
# Output: [-1]
# Explanation: There are no elements to the right of index 0.
 
from typing import List
def replace_elements( arr : List[int]) -> List[int]:
    mx = -1
    i = len(arr)-1
    while i >= 0:
        temp = arr[i]
        arr[i] = mx
        if temp > mx:
            mx = temp
        i -=1
    return arr

if __name__ == "__main__":
    #arr = [17,18,5,4,6,1]
    arr = [400]
    print ("{}".format(replace_elements(arr)))

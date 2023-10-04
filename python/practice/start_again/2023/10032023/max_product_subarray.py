# 152. Maximum Product Subarray
# Medium
# 17.4K
# 544
# Companies
# Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 
from typing import List
def max_product_subarray(nums: List[int]) -> int:
    currMax=1
    currMin=1
    result=nums[0]
    for n in nums:
        values=(n, n*currMax, n*currMin)
        currMax=max(values)
        currMin=min(values)
        result=max(result, currMax)
    return result

if __name__ == "__main__":
    #nums = [2,3,-2,4]
    nums = [-2,0,-1]
    print ("{}".format(max_product_subarray(nums)))

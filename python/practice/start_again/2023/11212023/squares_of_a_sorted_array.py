# #   https://leetcode.com/problems/squares-of-a-sorted-array/

# 977. Squares of a Sorted Array
# Easy
# 8.5K
# 211
# Companies
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 
from typing import List
def sortedSquares(nums: List[int]) -> List[int]:
    # Solution - 01 
    # return sorted( [v **2 for v in nums])
    
    # Solution - 02 

    for i in range(len(nums)):
        nums[i] *= nums[i]
    nums.sort()
    return nums



if __name__ == "__main__":
    nums = [-7,-3,2,3,11]
    print ("{}".format(sortedSquares(nums)))
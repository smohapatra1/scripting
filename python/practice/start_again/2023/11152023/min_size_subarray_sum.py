# #   https://leetcode.com/problems/minimum-size-subarray-sum/

# 209. Minimum Size Subarray Sum
# Medium
# 11.9K
# 366
# Companies
# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

from typing import List
from sys import maxsize
def minSize(nums: List[int], target: int ) -> int:
    res = maxsize
    left =0
    total =0
    for i in range(len(nums)):
        total+=nums[i]
        while total >=target:
            res = min(res, i-left +1)
            total -=nums[left]
            left +=1
    return res if res !=maxsize else 0

if __name__ == "__main__":
    target = 7
    nums = [2,3,1,2,4,3]
    print ("{}".format(minSize(nums, target)))

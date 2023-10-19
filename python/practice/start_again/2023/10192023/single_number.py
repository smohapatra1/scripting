# #   https://leetcode.com/problems/single-number/

# 136. Single Number
# Easy
# 15.4K
# 624
# Companies
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1

from typing import List
def single_number(nms: List[int]) -> int:
   return 2*sum(set (nums)) - sum(nums)
        

if __name__ == "__main__":
    #nums = [2,2,1]
    #nums = [4,1,2,1,2]
    nums = [1]
    print ("{}".format(single_number(nums)))

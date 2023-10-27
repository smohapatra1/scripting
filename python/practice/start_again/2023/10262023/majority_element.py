# #   https://leetcode.com/problems/majority-element/

# 169. Majority Element
# Easy
# 17.3K
# 514
# Companies
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
from typing import List
from typing import List
def majorityElement(nums: List[int]) -> int:
    nums.sort()
    n=len(nums)
    return nums[n//2]

if __name__ == "__main__":
    nums = [3,2,3]
    print ("{}".format(majorityElement(nums)))



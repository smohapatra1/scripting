# #   https://leetcode.com/problems/single-element-in-a-sorted-array/

# 540. Single Element in a Sorted Array
# Medium
# 10.5K
# 164
# Companies
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

 

# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10

from typing import List
def singleElement(nums: List[int]) -> int:
    left = 0 
    right = len(nums) - 1
    while left < right:
        mid = (left + right )//2
        if mid % 2 == 1:
            mid -=1
        if nums[mid] != nums[mid + 1]:
            right = mid 
        else:
            left = mid + 2
    return nums[left]
if __name__ == "__main__":
    nums = [1,1,2,3,3,4,4,8,8]
    print ("{}".format(singleElement(nums)))

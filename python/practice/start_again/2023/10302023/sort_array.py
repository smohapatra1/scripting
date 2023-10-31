# #   https://leetcode.com/problems/sort-an-array/
# 912. Sort an Array
# Medium
# 5.6K
# 723
# Companies
# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.
 
from typing import List
def sort_array(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums
    mid=len(nums)//2
    left = sort_array(nums[:mid])
    right=sort_array(nums[mid:])
    merged=[]
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)
    return merged 

if __name__ == "__main__":
    nums = [5,2,3,1]
    print ("The number post Sorting is {}".format(sort_array(nums)))
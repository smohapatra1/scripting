# #   https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# 34. Find First and Last Position of Element in Sorted Array
# Medium
# 19.5K
# 472
# Companies
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

from typing import List
def FirstLast( nums : List[int] , target=0) -> List[int]:
    # Solution - 01 
    # first = -1
    # last = -1 
    # for i in range(len(nums)):
    #     if nums[i] == target:
    #         if first == -1 :
    #             first = i
    #         last = i 
    # return [first, last ]
    def search(x):
        start = 0 
        end = len(nums)
        while start < end :
            mid = (start + end )//2
            if nums[mid] < x :
                start = mid + 1
            else:
                end = mid 
        return start 
    start = search(target)
    end = search((target+1))-1
    if start <= end:
        return [start, end]
    return [ -1, -1 ]

if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    print ("{}".format(FirstLast(nums, target)))

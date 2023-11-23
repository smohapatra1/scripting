# #   https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# 81. Search in Rotated Sorted Array II
# Medium
# 8K
# 986
# Companies
# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

# You must decrease the overall operation steps as much as possible.

 

# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
 

from typing import List
def searchArray(nums: List[int] , target : int ) -> bool:
    # nums.sort()
    # for i in nums:
    #     if i == target:
    #         return True
    # return False
    start = 0 
    end = len(nums) -1 
    while start <= end:
        mid = (start + end )//2
        if nums[mid] == target:
            return True
        if nums[mid] == nums[end]:
            end -=1
        elif nums[mid] > nums[end]:
            if nums[start] <=target and target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid]  < target and target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1 
    return False 

if __name__ == "__main__":
    nums = [2,5,6,0,0,1,2]
    target = 3
    print ("{}".format(searchArray(nums, target)))

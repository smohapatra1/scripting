# #   https://leetcode.com/problems/non-decreasing-array/

# 665. Non-decreasing Array
# Medium
# 5.6K
# 764
# Companies
# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

# Example 1:

# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:

# Input: nums = [4,2,1]
# Output: false
# Explanation: You cannot get a non-decreasing array by modifying at most one element.
 

from typing import List
def non_decreasing_array( nums: List[int]) -> bool:
    cnt=0
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            if cnt == 1:
                return False
            cnt+=1
        if i >=2 and nums[i-2] > nums[i]:
            nums[i] = nums[i-1]
    return True



if __name__ == "__main__":
    nums=[4,2,3]
    #nums = [4,2,1]
    print ("{}".format(non_decreasing_array(nums)))
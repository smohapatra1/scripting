# #   https://leetcode.com/problems/move-zeroes/
# 283. Move Zeroes
# Easy
# 15.6K
# 397
# Companies
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]

from typing import List
def move_zeros(nums: List[int]) -> List[int]:
    #Solution-01

    # anchor=0
    # for explorer in range(len(nums)):
    #     if nums[explorer] != 0:
    #         nums[anchor] = nums[explorer]
    #         nums[explorer] = nums[anchor]
    #         anchor +=1
    # Solution-02:
    n = len(nums)
    i=0
    for j in range(n):
        if (nums[j] != 0):
            nums[i], nums[j] = nums[j], nums[i]
            i+=1

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    print ("Pre move - {} and Post Move - {}".format(nums, move_zeros(nums)))

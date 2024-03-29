# #   https://leetcode.com/problems/sort-colors/

# 75. Sort Colors
# Medium
# 17K
# 587
# Companies
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]

from typing import List
def sort_colors(nums: List[int]) -> List[int]:
    red, white, blue=0, 0, len(nums)-1
    while white <= blue:
        if nums[white] ==0:
            nums[white] , nums[red] = nums[red], nums[white]
            red+=1
            white+=1
        elif nums[white] == 1:
            white +=1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue-=1

if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    print ("The number post Sorting is {}".format(sort_colors(nums)))

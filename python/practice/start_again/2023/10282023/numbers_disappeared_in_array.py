# #   https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# 448. Find All Numbers Disappeared in an Array
# Easy
# 9K
# 454
# Companies
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n



from typing import List
def nums_disappeared(nums: List[int]) -> List[int]:
    for i in nums:
        a = abs(i) - 1
        if nums[a] > 0:
            nums[a] *= -1
    return [i+1 for i, n in enumerate(nums) if n> 0 ]


if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    print ("{}".format(nums_disappeared(nums)))


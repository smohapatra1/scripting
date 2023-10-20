# #   https://leetcode.com/problems/concatenation-of-array/

# 1929. Concatenation of Array
# Easy
# 2.9K
# 337
# Companies
# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.

 

# Example 1:

# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]
# Example 2:

# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]

from typing import List
def concatenate_array( nums: List[int]) -> List[int]:
    #solution-01
    #return nums * 2
    #Solution-02
    n=len(nums)
    for i in range(n):
        nums.append(nums[i])
    return nums
if __name__ == "__main__":
    nums=[1,2,1]
    print ("{}".format(concatenate_array(nums)))
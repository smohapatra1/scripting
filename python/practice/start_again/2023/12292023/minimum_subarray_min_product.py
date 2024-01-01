# #   https://leetcode.com/problems/maximum-subarray-min-product/
# 1856. Maximum Subarray Min-Product
# Medium
# 1.4K
# 105
# Companies
# The min-product of an array is equal to the minimum value in the array multiplied by the array's sum.

# For example, the array [3,2,5] (minimum value is 2) has a min-product of 2 * (3+2+5) = 2 * 10 = 20.
# Given an array of integers nums, return the maximum min-product of any non-empty subarray of nums. Since the answer may be large, return it modulo 109 + 7.

# Note that the min-product should be maximized before performing the modulo operation. Testcases are generated such that the maximum min-product without modulo will fit in a 64-bit signed integer.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [1,2,3,2]
# Output: 14
# Explanation: The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
# 2 * (2+3+2) = 2 * 7 = 14.
# Example 2:

# Input: nums = [2,3,3,1,2]
# Output: 18
# Explanation: The maximum min-product is achieved with the subarray [3,3] (minimum value is 3).
# 3 * (3+3) = 3 * 6 = 18.
# Example 3:

# Input: nums = [3,1,5,6,4,2]
# Output: 60
# Explanation: The maximum min-product is achieved with the subarray [5,6,4] (minimum value is 4).
# 4 * (5+6+4) = 4 * 15 = 60.
 

from typing import List
def MinSubarray(nums: List[int]) -> int:
    mod=int(1e9+7)
    stack=[]
    rsum=0
    res=0
    nums.append(0)
    for i, v in enumerate(nums):
        while stack and nums[stack[-1][0]] >=v:
            index , _ = stack.pop()
            arrSum=rsum
            if stack:
                arrSum = rsum-stack[-1][1]
            res=max(res, nums[index]*arrSum)
        rsum+=v
        stack.append((i, rsum))
    return res%mod


if __name__ == "__main__":
    nums = [1,2,3,2]
    print ("{}".format(MinSubarray(nums)))

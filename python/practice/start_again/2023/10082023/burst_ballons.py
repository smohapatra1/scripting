# #   https://leetcode.com/problems/burst-balloons/
# 312. Burst Balloons
# Hard
# 8.5K
# 218
# Companies
# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

# Return the maximum coins you can collect by bursting the balloons wisely.

 

# Example 1:

# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
# Example 2:

# Input: nums = [1,5]
# Output: 10
from functools import lru_cache
from typing import List
def burst_balloons(nums: List[int]) -> int:
    nums=[1] + nums + [1]
    lru_cache(None)
    def dp(i, j ):
        if i > j : 
            return 0
        if i ==j :
            return nums[i-1] * nums[i] * nums[i+1]
        return max(dp(i, k-1) + dp(k+1, j) + nums[i-1] * nums[k] * nums[j+1] for k in range(i, j+1) )
    return dp(1, len(nums)-2)  


if __name__ == "__main__":
    nums = [3,1,5,8]
    print ("{}".format(burst_balloons(nums)))


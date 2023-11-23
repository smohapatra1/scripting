# #   https://leetcode.com/problems/split-array-largest-sum/
# 410. Split Array Largest Sum
# Hard
# 9.2K
# 191
# Companies
# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.

 

# Example 1:

# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
# Example 2:

# Input: nums = [1,2,3,4,5], k = 2
# Output: 9
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.

from typing import List
def splitArray(nums: List[int], k: int ) -> int:
    lo = max(nums)
    hi = sum(nums)
    while lo < hi:
        mid = (lo + hi )//2
        n = 1 
        now = 0 
        for x in nums:
            now += x
            if now > mid:
                now = x 
                n +=1
        if n <= k:
            hi = mid
        else:
            lo = mid + 1
    return lo


if __name__ == "__main__":
    nums = [7,2,5,10,8]
    k = 2
    print ("{}".format(splitArray(nums, k)))
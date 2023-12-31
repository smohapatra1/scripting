# #   https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/
# 2369. Check if There is a Valid Partition For The Array
# Medium
# 1.9K
# 190
# Companies
# You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

# We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:

# The subarray consists of exactly 2, equal elements. For example, the subarray [2,2] is good.
# The subarray consists of exactly 3, equal elements. For example, the subarray [4,4,4] is good.
# The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
# Return true if the array has at least one valid partition. Otherwise, return false.

 

# Example 1:

# Input: nums = [4,4,4,5,6]
# Output: true
# Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
# This partition is valid, so we return true.
# Example 2:

# Input: nums = [1,1,1,2]
# Output: false
# Explanation: There is no valid partition for this array.
 

from typing import List
def CheckValidPartition(nums: List[int]) -> bool:
    n=len(nums)
    if n == 1:
        return False
    dp = [ True, False, nums[0] == nums[1] if n > 1 else False]
    for i in range(2, n):
        current_dp = ( nums[i] == nums[i-1] and dp[1]) or \
                      (nums[i] == nums[i-1] == nums[i-2] and dp[0]) or \
                        (nums[i] - nums[i-1] == 1 and nums[i-1] - nums[i-2] == 1 and dp[0])
        dp[0], dp[1], dp[2] = dp[1], dp[2], current_dp
    return dp[2]    
    


if __name__ == "__main__":
    nums = [4,4,4,5,6]
    print ("{}".format(CheckValidPartition(nums)))
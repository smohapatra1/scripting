# #https://leetcode.com/problems/maximum-sum-circular-subarray/

# 918. Maximum Sum Circular Subarray
# Medium
# 6.4K
# 281
# Companies
# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

# Example 1:

# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.
# Example 2:

# Input: nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
# Example 3:

# Input: nums = [-3,-2,-3]
# Output: -2
# Explanation: Subarray [-2] has maximum sum -2.

from typing import List
def MaxSumSubarray(nums: List[int]) -> int:
    if max(nums) <=0:
        return max(nums)
    max_dp=[i for i in nums]
    min_dp=[i for i in nums]
    for i in range(1, len(nums)):
        if max_dp[i-1] > 0:
            max_dp[i] +=max_dp[i-1]
        if min_dp[i] < 0:
            min_dp[i] +=min_dp[i-1]
    return max(max(max_dp), sum(nums) - min(min_dp))


if __name__ == "__main__":
    nums = [1,-2,3,-2]
    print ("{}".format(MaxSumSubarray(nums)))
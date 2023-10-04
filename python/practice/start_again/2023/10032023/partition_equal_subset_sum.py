# #   https://leetcode.com/problems/partition-equal-subset-sum/
# 416. Partition Equal Subset Sum
# Medium
# 11.5K
# 208
# Companies
# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
 
from typing import List 
def equal_subset(nums: List[int]) -> bool:
    total_sum=sum(nums)
    # If total sum is ODD, we cant partition the array into two equal sum subsets
    if total_sum % 2 == 1:
        return False
    target_sum=total_sum//2
    #Initialize a boolean size
    dp=[False] * (total_sum+1)
    dp[0]=True
    for num in nums:
        for j in range(target_sum, num-1, -1):
            dp[j]=dp[j] or dp[j-num]
    return dp[target_sum]

if __name__ == "__main__":
    #nums = [1,5,11,5]
    nums = [1,2,3,5]
    print ("{}".format(equal_subset(nums)))
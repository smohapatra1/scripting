# 300. Longest Increasing Subsequence
# Medium
# 18.9K
# 357
# Companies
# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence
# .

 

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

from typing import List
def longest_subsequence(nums: List[int]) -> int:
    n=len(nums)
    dp=[0 for _ in range(n)]
    for i in range(1, n ):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp) +1

if __name__ == "__main__":
    #nums = [10,9,2,5,3,7,101,18]
    nums = [7,7,7,7,7,7,7]
    print ("{}".format(longest_subsequence(nums)))
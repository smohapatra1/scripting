# #   https://leetcode.com/problems/combination-sum-iv/

# 377. Combination Sum IV
# Medium
# 7.2K
# 644
# Companies
# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

# The test cases are generated so that the answer can fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
# Example 2:

# Input: nums = [9], target = 3
# Output: 0


from typing import List
def CombinationIV(nums: List[int], target: int ) -> int:
    dp = [0] * (target +1)
    dp[0] = 1
    for i in range(1, target +1):
        for num in nums:
            if i - num >=0:
                dp[i] +=dp[i-num]
    return dp[target]



if __name__ == "__main__":
    nums = [1,2,3]
    target = 4
    print ("{}".format(CombinationIV(nums, target)))
# #   https://leetcode.com/problems/integer-break/
# 343. Integer Break
# Medium
# 5K
# 431
# Companies
# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

# Return the maximum product you can get.

 

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# Example 2:

# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
 
def Integer_Break(n: int) -> int:
    dp=[0] * (n+1)
    dp[1] = 1 
    for i in range(2, n+1):
        dp[i]=-float('inf')
        for j in range(1, i):
            dp[i] = max(dp[i], j * (i-j), j * dp[i-j])
    return dp[n]

if __name__ == "__main__":
    n=2
    print("{}".format(Integer_Break(n)))
# 115. Distinct Subsequences
# Hard
# 6.2K
# 273
# Companies
# Given two strings s and t, return the number of distinct subsequences of s which equals t.

# The test cases are generated so that the answer fits on a 32-bit signed integer.

 

# Example 1:

# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from s.
# rabbbit
# rabbbit
# rabbbit
# Example 2:

# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from s.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag

from typing import List
def dist_subsequence(s: str, t: str) -> int:
    m=len(s)
    n=len(t)
    dp=[[0] * (n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0]=1
    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] +=dp[i-1][j]
            if s[i-1] == t[j-1]:
                dp[i][j] +=dp[i-1][j-1]
    return dp[-1][-1]

if __name__ == "__main__":
    # s = "rabbbit"
    # t = "rabbit"
    s = "babgbag"
    t = "bag"
    print ("{}".format(dist_subsequence(s,t)))


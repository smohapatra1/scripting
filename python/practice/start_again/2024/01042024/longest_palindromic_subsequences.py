# #   https://leetcode.com/problems/longest-palindromic-subsequence/

# 516. Longest Palindromic Subsequence
# Medium
# 9.2K
# 316
# Companies
# Given a string s, find the longest palindromic subsequence's length in s.

# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".
# Example 2:

# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".

def LongestPalindromic(s: str) -> int:
    t=s[::-1]
    dp=[[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
    for i in range(1, len(s)+1):
        for j in range(1, len(s)+1):
            if s[i-1] != t[j-1]:
                dp[i][j]=max(dp[i][j-1], dp[i-1][j])
            else:
                dp[i][j]= 1+ dp[i-1][j-1]
    return dp[-1][-1]


if __name__ == "__main__":
    s = "bbbab"
    print ("{}".format(LongestPalindromic(s)))
# #   https://leetcode.com/problems/unique-binary-search-trees/
# 96. Unique Binary Search Trees
# Medium
# 10.1K
# 387
# Companies
# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

# Example 1:


# Input: n = 3
# Output: 5
# Example 2:

# Input: n = 1
# Output: 1

def numTrees(n: int )-> int:
    dp= [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        for j in range(i):
            dp[i] +=dp[j] * dp[i-1-j]
    return dp[n]
    if n == 1:
        return n

if __name__ == "__main__":
    n= 5
    print ("{}".format(numTrees(n)))
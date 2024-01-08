# #   https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/
# 2218. Maximum Value of K Coins From Piles
# Hard
# 2.2K
# 36
# Companies
# There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.

# In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.

# Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.

 

# Example 1:


# Input: piles = [[1,100,3],[7,8,9]], k = 2
# Output: 101
# Explanation:
# The above diagram shows the different ways we can choose k coins.
# The maximum total we can obtain is 101.
# Example 2:

# Input: piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
# Output: 706
# Explanation:
# The maximum total can be obtained if we choose all coins from the last pile.
 
from typing import List
from functools import lru_cache
def MaxValueKcoins(piles: List[List[int]], k : int ) -> int:
    @lru_cache(None)
    def dp(i, K):
        if k ==0 or i == len(piles):
            return 0
        res = dp(i+1, K)
        cur = 0 
        for j in range(min(len(piles[i]), K )):
            cur +=piles[i][j]
            res=max(res, cur + dp(i+1, K-j-1))
        return res
    return dp(0, k)


if __name__ == "__main__":
    piles = [[1,100,3],[7,8,9]]
    k = 2
    print ("{}".format(MaxValueKcoins(piles, k)))

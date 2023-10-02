# #   https://leetcode.com/problems/coin-change/
# 322. Coin Change
# Medium
# 17.8K
# 401
# Companies
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0

from typing import List
def coin_change(coins: List[int], amount:int ) -> None:
    dp = [0] * (amount +1)
    for i in range(1, amount +1 ):
        if i in coins:
            dp[i] = 1
            continue
        min_coins = float("inf")
        for coin in coins:
            if i-coin >=0:
                min_coins=min(dp[i-coin], min_coins)
        dp[i] = min_coins +1
    if dp[-1] == float("inf"):
        return -1
    return dp[-1] 



if __name__ == "__main__":
    #coins = [1,2,5]
    #amount = 11 # To be made ( fewest number) from the above list of coins 
    coins = [2]
    amount = 3
    print ("{}".format(coin_change(coins, amount)))
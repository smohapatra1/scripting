# 309. Best Time to Buy and Sell Stock with Cooldown
# Medium
# 9K
# 292
# Companies
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

# Example 1:

# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# Example 2:

# Input: prices = [1]
# Output: 0

from typing import List
def bestProfit(prices : List[int]) -> int:
    sell=0
    cool_down=0
    hold=-float('inf')
    for stock_price in prices:
        prev_hold=hold
        prev_sell=sell
        prev_cool_down=cool_down
        cool_down=max(prev_cool_down, prev_sell)
        sell=prev_hold + stock_price
        hold=max(prev_hold, prev_cool_down - stock_price)
    return (max(sell, cool_down))




if __name__ == "__main__":
    #prices = [1,2,3,0,2]
    prices = [1]
    print ("{}".format(bestProfit(prices)))



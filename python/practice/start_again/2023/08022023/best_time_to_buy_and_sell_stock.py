# 121. Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

#   Steps :- 
#   Initialize all variables 
#   Write a while loop until right pointer is less than the length of array
#   If price [ left ] is greater than price [right], move the left pointer to the right position and increment our right pointer by 1
#   If price [ left ] is less than price [right], means we have profit so will update our max_profit and move our right pointer
#   If price [ left ] is less than price [ right ], so we have profit. We will check our max profit
#      


def buy_sell_stock(prices):
    # Lets initialize all variables 
    n=len(prices)
    left=0 # Buy
    right=1 # Sell
    max_profit=0 
    while right < n:
        current_profit = prices[right] - prices[left]
        if prices[left] < prices [right]:
            max_profit =max(current_profit, max_profit)
        else:
            left = right
        right +=1
    return max_profit

if __name__ == "__main__":
    prices=[7,1,5,3,6,4]
    #prices=[[7,6,4,3,1]]
    print("Best day to sell and buy the stock is {}".format(buy_sell_stock(prices)))
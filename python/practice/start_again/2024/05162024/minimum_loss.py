# #   https://www.hackerrank.com/challenges/minimum-loss/problem?isFullScreen=true

# Lauren has a chart of distinct projected prices for a house over the next several years. She must buy the house in one year and sell it in another, and she must do so at a loss. She wants to minimize her financial loss.

# Example

# Her minimum loss is incurred by purchasing in year  at  and reselling in year  at . Return .

# Function Description

# Complete the minimumLoss function in the editor below.

# minimumLoss has the following parameter(s):

# int price[n]: home prices at each year
# Returns

# int: the minimum loss possible
# Input Format

# The first line contains an integer , the number of years of house data.
# The second line contains  space-separated long integers that describe each .

# Constraints

# All the prices are distinct.
# A valid answer exists.
# Subtasks

#  for  of the maximum score.
# Sample Input 0

# 3
# 5 10 3
# Sample Output 0

# 2
# Explanation 0

# Lauren buys the house in year  at  and sells it in year  at  for a minimal loss of .

# Sample Input 1

# 5
# 20 7 8 2 5
# Sample Output 1

# 2
# Explanation 1

# Lauren buys the house in year  at  and sells it in year  at  for a minimal loss of .


def minimumLoss(price):
    priceS = sorted([(p, i ) for i, p in enumerate(price)])
    return min([priceS[i+1][0] - priceS[i][0] for i in range(len(priceS)-1) if priceS[i+1][1] < priceS[i][1]])

if __name__ == "__main__":
    n = int(input().strip())
    price = list(map(int, input().rstrip().split()))
    result = minimumLoss(price)
    print (result)

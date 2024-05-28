# #   https://www.hackerrank.com/challenges/the-blacklist/problem?isFullScreen=true

# A new gangster is trying to take control of the city. He makes a list of his  adversaries (e.g. gangster , gangster , ... gangster , gangster ) and plans to get rid of them.

#  mercenaries are willing to do the job. The gangster can use any number of these mercenaries. But he has to honor one condition set by them: they have to be assigned in such a way that they eliminate a consecutive group of gangsters in the list, e.g. gangster , gangster , ..., gangster , gangster , where the following is true: .

# While our new gangster wants to kill all of them, he also wants to pay the least amount of money. All mercenaries charge a different amount to kill different people. So he asks you to help him minimize his expenses.

# Input Format

# The first line contains two space-separated integers,  and . Then  lines follow, each containing  integers as follows:
# The th number on the th line is the amount charged by the th mercenary for killing the th gangster on the list.

# Constraints

 
# Output Format

# Just one line, the minimum cost for killing the  gangsters on the list.

# Sample Input

# 3 2
# 1 4 1
# 2 2 2
# Sample Output

#  5
# Explanation

# The new gangster can assign mercenary 1 to kill gangster 1, and mercenary 2 to kill gangster 2 and gangster 3.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'blacklist' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY amounts as parameter.
#

N, K = map(int, input().split())
cost = []

MASK = 2<<K
INF = 10**8-1

for i in range(K):
    prices = list (map(int, input().split()))
    prices.reverse()
    cost.append(prices)

dp = []
for i in range(MASK):
    dp.append([INF] * (N + 1))

dp[0][0] = 0

def hitman_available(hitman, mask):
    return not (2 << hitman) & mask

def use_hitman(hitman, mask):
    return mask | (2 << hitman)

for already_killed in range(N):
    for mask in range(MASK):
        for hitman in range(K):
            if hitman_available(hitman, mask):
                mask_after = use_hitman(hitman, mask)
                for num_to_kill in range(1, N - already_killed+1):
                    dp[mask_after][num_to_kill + already_killed] = min(
                        dp[mask_after][num_to_kill + already_killed],
                        dp[mask][already_killed] + sum(cost[hitman][already_killed:already_killed+num_to_kill]))

print (min(dp[i][N] for i in range(MASK)))

# def blacklist(amounts):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     k = int(first_multiple_input[1])

#     amounts = []

#     for _ in range(k):
#         amounts.append(list(map(int, input().rstrip().split())))

#     result = blacklist(amounts)

#     fptr.write(str(result) + '\n')

#     fptr.close()

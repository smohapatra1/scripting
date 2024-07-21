# #       https://www.hackerrank.com/challenges/taste-of-win/problem?isFullScreen=true

# Stephanie just learned about a game called Nim in which there are two players and  piles of stones. During each turn, a player must choose any non-empty pile and take as many stones as they want. The first player who cannot complete their turn (i.e., because all piles are empty) loses.

# Stephanie knows that, for each start position in this game, it's possible to know which player will win (i.e., the first or second player) if both players play optimally. Now she wants to know the number of different games that exist that satisfy all of the following conditions:

# The game starts with  non-empty piles and each pile contains less than  stones.
# All the piles contain pairwise different numbers of stones.
# The first player wins if that player moves optimally.
# Help Stephanie by finding and printing the number of such games satisfying all the above criteria, modulo .

# Input Format

# The first line contains two space-separated integers describing the respective values of  and .

# Constraints

# Output Format

# Print the number of such games, modulo .

# Sample Input 0

# 2 2
# Sample Output 0

# 6
# Explanation 0

# We want to know the number of games with  piles where each pile contains  stones. There are six such possible games with the following distributions of stones: . Thus, we print the result of  as our answer.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'tastesLikeWinning' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def tastesLikeWinning(n, m):
    # Write your code here
    mod = 1000000007

    def qk_pow(b, t):
        res = 1
        tmp = b
        while t > 0:
            if t % 2 == 1:
                res = (res * tmp) % mod
            tmp = (tmp * tmp) % mod
            t //= 2
        return res
    base = qk_pow(2, m) - 1
    p2 = p1 = base
    f0 = 1
    f2 = f1 = 0
    for i in range(1, n):
        p2 = (p1 * (base-i)) % mod
        f2 = (p1 - f1 - (i * f0 % mod)*(base - i + 1) % mod) % mod
        p1 = p2
        f0 = f1
        f1 = f2
    return ((p2 - f2) % mod + mod) % mod

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = tastesLikeWinning(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()

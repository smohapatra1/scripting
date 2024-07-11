# #   https://www.hackerrank.com/challenges/chocolate-in-box/problem?isFullScreen=true

# Dexter and Debra are playing a game. They have N containers each having one or more chocolates. Containers are numbered from 1 to N, where ith container has A[i] number of chocolates.

# The game goes like this. First player will choose a container and take one or more chocolates from it. Then, second player will choose a non-empty container and take one or more chocolates from it. And then they alternate turns. This process will continue, until one of the players is not able to take any chocolates (because no chocolates are left). One who is not able to take any chocolates loses the game. Note that player can choose only non-empty container.

# The game between Dexter and Debra has just started, and Dexter has got the first Chance. He wants to know the number of ways to make a first move such that under optimal play, the first player always wins.

# Input Format

# The first line contains an integer N, i.e., number of containers.
# The second line contains N integers, i.e., number of chocolates in each of the containers separated by a single space.

# Constraints

# 1 ≤ N ≤ 106
# 1 ≤ A[i] ≤ 109

# Output Format

# Print the number of ways to make the first move such that under optimal play, the first player always wins. If the first player cannot win under optimal play, print 0.

# Sample Input

# 2
# 2 3
# Sample Output

# 1
# Explanation

# Only 1 set of moves helps player 1 win.

# Player:      1      2      1      2      1
# Chocolates: 2 3 -> 2 2 -> 1 2 -> 1 1 -> 0 1


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateInBox' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

from functools import reduce
import operator

n = int(input())
a = list(map(int, input().split()))

gr = reduce(operator.xor, a)
ans = sum(1 for _ in filter(lambda x: x ^ gr < x, a))
print(ans)


# def chocolateInBox(arr):
#     # Write your code here
    
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     arr_count = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     result = chocolateInBox(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()

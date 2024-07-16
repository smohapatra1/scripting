# #   https://www.hackerrank.com/challenges/chessboard-game-again-1/problem?isFullScreen=true

# Two players are playing a game on a  chessboard. The rules of the game are as follows:

# The game starts with  coins located at one or more  coordinates on the board (a single cell may contain more than one coin). The coordinate of the upper left cell is , and the coordinate of the lower right cell is .
# In each move, a player must move a single coin from some cell  to one of the following locations:

# .
# Note: The coin must remain inside the confines of the board.

# The players move in alternating turns. The first player who is unable to make a move loses the game.

# The figure below shows all four possible moves:

# chess

# Note: While the figure shows a  board, this game is played on a  board.

# Given the value of  and the initial coordinate(s) of  coins, determine which player will win the game. Assume both players always move optimally.

# Input Format

# The first line contains an integer, , denoting the number of test cases.
# Each test case is defined as follows over the subsequent lines:

# The first line contains an integer, , denoting the number of coins on the board.
# Each line  (where ) of the  subsequent lines contains  space-separated integers describing the respective values of  and  of the coordinate where coin  is located.
# Note: Recall that a cell can have more than one coin (i.e., any cell can have  to  coins in it at any given time).

# Constraints

# , where .
# Output Format

# On a new line for each test case, print  if the first player is the winner; otherwise, print .

# Sample Input

# 2
# 3
# 5 4
# 5 8
# 8 2
# 6
# 7 1
# 7 2
# 7 3
# 7 4
# 7 4
# 7 4
# Sample Output

# First
# Second


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chessboardGame' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY coins as parameter.
#

from functools import reduce
from operator import xor
gnum = [[-1] * 17 for _ in range(17)]
for s in range(2, 31):
    for j in range(max(1, s - 15), min(16, s)):
        i = s - j
        target = ((i - 1, j - 2), (i + 1, j - 2), (i - 2, j - 1), (i - 2, j + 1))
        nextval = {gnum[x][y] for x, y in target}
        gnum[i][j] = next(i for i in range(100) if i not in nextval)
for _ in range(int(input())):
     print("First" if reduce(xor, (gnum[x][y] for x, y in (map(int, input().split()) for _ in range(int(input())))), 0) else "Second")
     

# def chessboardGame(coins):
#     # Write your code here
#     res = 0 
#     for Y in coins:
#         x = Y[0] -1
#         y = Y[1]-1
#         res ^= x
#     return 'Second' if res == 0 else 'First'

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         k = int(input().strip())

#         coins = []

#         for _ in range(k):
#             coins.append(list(map(int, input().rstrip().split())))

#         result = chessboardGame(coins)

#         fptr.write(result + '\n')

#     fptr.close()

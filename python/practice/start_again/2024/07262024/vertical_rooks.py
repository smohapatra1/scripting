# #   https://www.hackerrank.com/challenges/vertical-rooks/problem?isFullScreen=true

# HackerChess is a variant of chess played at HackerRank. It is a game played between two players who make moves in turns until one of them cannot make any move. The player who cannot make a move loses the game and the other player is declared the winner. The game is played on a board with  rows and  columns. The only pieces used in the game are rooks. A rook in HackerChess moves only vertically, which means that in never leaves a column to which it belongs. Moreover, in a single move, a rook moves through any number of unoccupied cells. Notice that there are no captures in HackerChess, two rooks cannot occupy the same cell, and a rook cannot jump over another rook. Each player has exactly one rook in each of the  columns of the board.

# Given the initial position of the rooks and knowing that the second player makes the first move, decide who will win the game if both players play optimally.

# Input Format

# In the first line, there is a single integer  denoting the number of games to be played. After that, descriptions of  games follow:

# In the first line, there is a single integer  denoting the size of the board. Next,  lines follow. In the -th of them there is a single integer  denoting the row of the rook belonging to the first player placed in the -th column. After that, another  lines follow. In the -th of them there is a single integer  denoting the row of the rook belonging to the second player placed in the -th column.

# Constraints

# Output Format

# Print exactly  lines. In the -th of them, print player-1 if the first player will win the -th game. Otherwise, print player-2 in this line.

# Sample Input 0

# 1
# 3
# 1
# 2
# 2
# 3
# 1
# 1
# Sample Output 0

# player-2
# Explanation 0

# There is only one game player in the sample input. The game is played on the board with  rows and  columns. Let's denote the first player's rooks as red rooks and the second player's rooks as green ones. Then the initial position of the game looks like this:

# image

# The second player moves first and he can move his rook in the first column to the second row. After this move, the position looks as follows:

# image

# Next, it is the first player's turn. He cannot make any move with his rook in the first column, so he has to make a move in the second or the third column. Without the loss of generality, let's assume that he makes a move in the second column. He can only make one such move, i.e. move the rook from the second to the third row. This results in the following position:

# image

# After that, the best move for the second player is to move his rook in the second column from the first to the second row. After this move, the position looks like this:

# image

# Next, it is again the first player's move. The only move he can make is to move his rook in the third column from the second to the third row. It results in the following position:

# image

# Then, the best move for the second player is to move his rook in the third column from the first to the second row. After that, the position looks as follows:

# image

# Next, it is the first player's move, but since he is unable to make any valid move, he loses and the second player is declared a winner.

# It shows that regardless of the first player's moves, the second player has a strategy leading to his victory.

# Sample Input 1

# 1
# 4
# 3
# 3
# 3
# 3
# 4
# 4
# 4
# 4
# Sample Output 1

# player-1
# Explanation 1

# Second player cannot make a move so  is the winner.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'verticalRooks' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY r1
#  2. INTEGER_ARRAY r2
#

from functools import reduce

def processTestCase():
    n = int(input())
    p1 = [int(input()) for i in range(n)]
    p2 = [int(input()) for i in range(n)]
    p = [ abs(p1[i]-p2[i]) - 1 for i in range(n)]
    nimsum = reduce(lambda x,y : x^y, p)
    if nimsum is 0:
        print('player-1')
    else:
        print('player-2')

t = int(input())

for i in range(t):
    processTestCase()

# def verticalRooks(r1, r2):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         n = int(input().strip())

#         r1 = []

#         for _ in range(n):
#             r1_item = int(input().strip())
#             r1.append(r1_item)

#         r2 = []

#         for _ in range(n):
#             r2_item = int(input().strip())
#             r2.append(r2_item)

#         result = verticalRooks(r1, r2)

#         fptr.write(result + '\n')

#     fptr.close()

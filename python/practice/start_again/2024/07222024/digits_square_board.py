# #   https://www.hackerrank.com/challenges/digits-square-board-1/problem?isFullScreen=true

# Two HackerRank staffers found a secret room with a mysterious  square board and decided to play a game with it. The game has the following rules:

# At the beginning of the game, the players write a single digit (given as input) ranging from  to  in each  cell composing the  square board.
# The players move in alternating turns. In each move, the current player performs the following actions:

# Chooses a board that has at least one non-prime number written on it and has more than one cell (i.e., dimensions ).
# Cuts the chosen board into  smaller boards by breaking it along any horizontal or vertical line at the edge of a cell.
# Note: Although the game starts with one  board, that board is split in two during each move. At the beginning of the  move, a player can choose any one of the  pieces of the original board (as long as it can have a legal move performed on it).

# The game ends when there are no more cuttable boards (i.e., there are  boards, or all boards have only prime numbers written on them). The first player who is unable to make a move loses.

# Given the value of  and the respective numbers written in each  cell of the board, determine whether the person who wins the game is the first or second person to move. Assume both players move optimally.

# Time Limit

# Python: 18 seconds
# Pypy2: 5 seconds
# For other languages, the time limit is standard.

# Input Format

# The first line contains an integer, , denoting the number of test cases.
# Each test case is defined as follows over the subsequent lines:

# An integer, , denoting the length of each of the board's sides.
# Each line  of the  subsequent lines contains  space-separated integers describing , where each  describes the number written in cell  of the board.
# Constraints

# Output Format

# For each test case, print the name of the player with the winning strategy on a new line (i.e., either  or ).

# Sample Input

# 2
# 3
# 2 7 5
# 2 7 5
# 7 7 7
# 2
# 4 3
# 1 2
# Sample Output

# Second
# First
# Explanation

# We'll refer to the two players as  and .

# Test Case 0:
# All cells contain prime numbers, so there are no valid moves available to . As  wins by default, we print  on a new line.

# Test Case 1:
# In this test case, the two players perform the following sequence of moves:

#  makes a horizontal cut, splitting the board into two  boards. This is demonstrated in the following diagram: square

#  now chooses one of the two  rectangles and cuts it vertically, splitting it into two  squares.

#  chooses remaining  rectangle and cuts it vertically, splitting it into two  squares.
# After the above  moves take place, the board is split into four  squares and no more moves are available for  to make. Thus,  wins and we print  on a new line.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squareBoard' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY board as parameter.
#

def squareBoard(board):
    # Write your code here
    n = len(board)
    for row in board:
        row[:] = [x not in [2, 3, 5, 7] for x in row]
    sq = [[0 for y in range(n+1)] for x in range(n+1)]
    for x in range(n):
        for y in range(n):
            sq[x+1][y+1] = sq[x+1][y] + board[x][y]
    for y in range(n):
        for x in range(n):
            sq[x+1][y+1] += sq[x][y+1]
    dp = [[[[0 for h in range(n - y + 1)]
            for w in range(n - x + 1)]
            for y in range(n)]
            for x in range(n)]
    for w in range(1, n + 1):
        for h in range(1, n + 1):
            for x in range(n - w + 1):
                for y in range(n - h + 1):
                    if sq[x+w][y+h] + sq[x][y] - sq[x][y+h] - sq[x+w][y]:
                        seen = [False] * (2 * n - 1)
                        for ww in range(1, w):
                            seen[dp[x][y][ww][h] ^ dp[x+ww][y][w-ww][h]] = True
                        for hh in range(1, h):
                            seen[dp[x][y][w][hh] ^ dp[x][y+hh][w][h-hh]] = True
                        dp[x][y][w][h] = seen.index(False)
    return 'First' if dp[0][0][n][n] else 'Second'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        board = []

        for _ in range(n):
            board.append(list(map(int, input().rstrip().split())))

        result = squareBoard(board)

        fptr.write(result + '\n')

    fptr.close()

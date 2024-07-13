# #   https://www.hackerrank.com/challenges/a-chessboard-game-1/problem?isFullScreen=true

# Two players are playing a game on a  chessboard. The rules of the game are as follows:

# The game starts with a single coin located at some  coordinates. The coordinates of the upper left cell are , and of the lower right cell are .

# In each move, a player must move the coin from cell  to one of the following locations:

# Note: The coin must remain inside the confines of the board.

# Beginning with player 1, the players alternate turns. The first player who is unable to make a move loses the game.

# The figure below shows all four possible moves using an  board for illustration:

# chess(1)

# Given the initial coordinates of the players' coins, assuming optimal play, determine which player will win the game.

# Function Description

# Complete the chessboardGame function in the editor below. It should return a string, either First or Second.

# chessboardGame has the following parameter(s):

# x: an integer that represents the starting column position
# y: an integer that represents the starting row position
# Input Format

# The first line contains an integer , the number of test cases.
# Each of the next  lines contains  space-separated integers  and .

# Constraints

# Output Format

# On a new line for each test case, print  if the first player is the winner. Otherwise, print .

# Sample Input

# 3
# 5 2
# 5 3
# 8 8
# Sample Output

# Second
# First
# First
# Explanation

# In the first case, player1 starts at the red square and can move to any of the blue squares. Regardless of which one is chosen, the player 2 can move to one of the green squares to win the game.

# image

# In the second case, player 1 starts at the red square and can move to any of the blue squares or the purple one. Moving to the purple one limits player 2 to the yellow square. From the yellow square, player 1 moves to the green square and wins.

# image


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
# The function accepts following parameters:
#  1. INTEGER x
#  2. INTEGER y
#

def chessboardGame(x, y):
    # Write your code here
    if (((x-1) % 4 >= 0 and (x-1) % 4 <= 1) and ((y-1) % 4 >= 0 and (y-1) % 4 <= 1)):
        return "Second"
    else:
        return "First"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        x = int(first_multiple_input[0])

        y = int(first_multiple_input[1])

        result = chessboardGame(x, y)

        fptr.write(result + '\n')

    fptr.close()

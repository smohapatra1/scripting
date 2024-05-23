# #   https://www.hackerrank.com/challenges/coin-on-the-table/problem?isFullScreen=true

# You have a rectangular board consisting of  rows, numbered from  to , and  columns, numbered from  to . The top left is  and the bottom right is . Initially - at time  - there is a coin on the top-left cell of your board. Each cell of your board contains one of these letters:

# *: Exactly one of your cells has letter '*'.

# U: If at time  the coin is on cell  and cell  has letter 'U', the coin will be on cell  at time , if . Otherwise, there is no coin on your board at time .

# L: If at time  the coin is on cell  and cell  has letter 'L', the coin will be on cell  at time , if . Otherwise, there is no coin on your board at time .

# D: If at time  the coin is on cell  and cell  has letter 'D', the coin will be on cell  at time , if . Otherwise, there is no coin on your board at time .

# R: If at time  the coin is on cell  and cell  has letter 'R', the coin will be on cell  at time , if . Otherwise, there is no coin on your board at time .

# When the coin reaches a cell that has letter '*', it will stay there permanently. When you punch on your board, your timer starts and the coin moves between cells. Before starting the game, you can make operations to change the board, such that you are sure that at or before time  the coin will reach the cell having letter '*'. In each operation you can select a cell with some letter other than '*' and change the letter to 'U', 'L', 'R' or 'D'. You need to carry out as few operations as possible in order to achieve your goal. Your task is to find the minimum number of operations.

# For example, given a grid of  rows and  columns:

# UDL
# RR*
# the goal is to get from  to  in as few steps as possible. As the grid stands, it cannot be done because of the U in the cell at . If  is changed to D, the path  is available. It could also be changed to R which would make the path  available. Either choice takes  change operation, which is the value sought if . A lower value of  would result in a return value of  because the shortest path is  steps, starting from .

# Function Description

# Complete the coinOnTheTable function in the editor below. It should return an integer that represents the minimum operations to achieve the goal, or  if it is not possible.

# coinOnTheTable has the following parameters:

# m: an integer, the number of columns on the board
# k: an integer, the maximum time to reach the goal
# board: an array of strings where each string represents a row of the board
# Input Format

# The first line of input contains three integers, , , and , the number of rows, the number of columns and the maximum time respectively.

# The next  lines contain  letters each, describing your board.

# Constraints



# Output Format

# Print an integer which represents the minimum number of operations required to achieve your goal. If you cannot achieve your goal, print .

# Sample Input

# 2 2 3  
# RD  
# *L
# Sample output :

# 0
# Sample input :

# 2 2 1  
# RD  
# *L
# Sample output :

# 1
# Explanation :

# In the first example, a valid path exists without making any changes. In the second example, the letter of cell (1,1) must be changed to 'D' to make a valid path. In each example, a path length  is available.

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'coinOnTheTable' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER k
#  3. STRING_ARRAY board
#
def find_symbol(board, symbol):
    for r, row in enumerate(board):
        for c, val in enumerate(row):
            if val == symbol:
                return r, c


def bfs(board, limit, end, min_distance):
    rows, cols = len(board), len(board[0])
    queue = deque([((0, 0), 0, 0)])
    moves = {'U': (-1, 0), 'L': (0, -1), 'D': (1, 0), 'R': (0, 1)}
    seen = {(0, 0): {0: 0}}
    least_changes = min_distance
    while queue:
        (r, c), changes, steps = queue.popleft()
        if steps > limit:
            continue
        if (r, c) == end:
            least_changes = min(changes, least_changes)
        for move, (y, x) in moves.items():
            rr, cc = r + y, c + x
            if 0 <= rr < rows and 0 <= cc < cols:
                new_changes = changes + (1 if board[r][c] != move else 0)
                new_state = ((rr, cc), new_changes, steps + 1)
                if (rr, cc) in seen:
                    if new_changes in seen[(rr, cc)]:
                        if steps + 1 < seen[(rr, cc)][new_changes]:
                            seen[(rr, cc)][new_changes] = steps + 1
                            queue.append(new_state)
                    else:
                        seen[(rr, cc)][new_changes] = steps + 1
                        queue.append(new_state)
                else:
                    seen[(rr, cc)] = {}
                    seen[(rr, cc)][new_changes] = steps + 1
                    queue.append(new_state)
    return least_changes

def coinOnTheTable(m, k, board):
    # Write your code here
    start, end = (0, 0), find_symbol(board, '*')
    min_distance = sum(abs(x - y) for x, y in zip(start, end))
    if min_distance > k:
        return -1
    return bfs(board, k, end, min_distance)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    board = []

    for _ in range(n):
        board_item = input()
        board.append(board_item)

    result = coinOnTheTable(m, k, board)

    fptr.write(str(result) + '\n')

    fptr.close()

# #   https://www.hackerrank.com/challenges/bomber-man/problem?isFullScreen=true

# Bomberman lives in a rectangular grid. Each cell in the grid either contains a bomb or nothing at all.

# Each bomb can be planted in any cell of the grid but once planted, it will detonate after exactly 3 seconds. Once a bomb detonates, it's destroyed — along with anything in its four neighboring cells. This means that if a bomb detonates in cell , any valid cells  and  are cleared. If there is a bomb in a neighboring cell, the neighboring bomb is destroyed without detonating, so there's no chain reaction.

# Bomberman is immune to bombs, so he can move freely throughout the grid. Here's what he does:

# Initially, Bomberman arbitrarily plants bombs in some of the cells, the initial state.
# After one second, Bomberman does nothing.
# After one more second, Bomberman plants bombs in all cells without bombs, thus filling the whole grid with bombs. No bombs detonate at this point.
# After one more second, any bombs planted exactly three seconds ago will detonate. Here, Bomberman stands back and observes.
# Bomberman then repeats steps 3 and 4 indefinitely.
# Note that during every second Bomberman plants bombs, the bombs are planted simultaneously (i.e., at the exact same moment), and any bombs planted at the same time will detonate at the same time.

# Given the initial configuration of the grid with the locations of Bomberman's first batch of planted bombs, determine the state of the grid after  seconds.

# For example, if the initial grid looks like:

# ...
# .O.
# ...
# it looks the same after the first second. After the second second, Bomberman has placed all his charges:

# OOO
# OOO
# OOO
# At the third second, the bomb in the middle blows up, emptying all surrounding cells:

# O.O
# ...
# O.O
# Function Description

# Complete the bomberMan function in the editory below.

# bomberMan has the following parameter(s):

# int n: the number of seconds to simulate
# string grid[r]: an array of strings that represents the grid
# Returns

# string[r]: n array of strings that represent the grid in its final state
# Input Format

# The first line contains three space-separated integers , , and , The number of rows, columns and seconds to simulate.
# Each of the next  lines contains a row of the matrix as a single string of  characters. The . character denotes an empty cell, and the O character (ascii 79) denotes a bomb.

# Constraints

# Subtask

#  for  of the maximum score.
# Sample Input

# STDIN           Function
# -----           --------
# 6 7 3           r = 6, c = 7, n = 3
# .......         grid =['.......', '...O...', '....O..',\
# ...O...                '.......', 'OO.....', 'OO.....']
# ....O..
# .......
# OO.....
# OO.....
# Sample Output

# OOO.OOO
# OO...OO
# OOO...O
# ..OO.OO
# ...OOOO
# ...OOOO
# Explanation

# The initial state of the grid is:

# .......
# ...O...
# ....O..
# .......
# OO.....
# OO.....
# Bomberman spends the first second doing nothing, so this is the state after 1 second:

# .......
# ...O...
# ....O..
# .......
# OO.....
# OO.....
# Bomberman plants bombs in all the empty cells during his second second, so this is the state after 2 seconds:

# OOOOOOO
# OOOOOOO
# OOOOOOO
# OOOOOOO
# OOOOOOO
# OOOOOOO
# In his third second, Bomberman sits back and watches all the bombs he planted 3 seconds ago detonate. This is the final state after  seconds:

# OOO.OOO
# OO...OO
# OOO...O
# ..OO.OO
# ...OOOO
# ...OOOO



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    # Write your code here
    row = len(grid)
    col = len(grid[0])
    if n < 2 :
        return grid
    if n % 2 == 0: 
        return ['O' * col for _ in range(row)]
    def boom():
        g = [list(i) for i in grid]
        for i in range(row):
            for j in range(col):
                if g[i][j] == 'O':
                    for x, y in (i, j+1), (i, j-1), (i+1, j ), (i-1, j ):
                        if 0 <= x < row and 0 <= y < col and g[x][y] == '.':
                            g[x][y] = 'X'
                    g[i][j] = 'X'
        return [''.join('.' if j == 'X' else 'O' for j in i) for i in g]
    grid = boom()
    return grid if n % 4 ==3 else boom() 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

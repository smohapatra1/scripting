# #   https://www.hackerrank.com/challenges/one-month-preparation-kit-castle-on-the-grid/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-four

# You are given a square grid with some cells open (.) and some blocked (X). Your playing piece can move along any row or column until it reaches the edge of the grid or a blocked cell. Given a grid, a start and a goal, determine the minmum number of moves to get to the goal.

# Example.






# The grid is shown below:

# ...
# .X.
# ...
# The starting position  so start in the top left corner. The goal is . The path is . It takes  moves to reach the goal.

# Function Description
# Complete the minimumMoves function in the editor.

# minimumMoves has the following parameter(s):

# string grid[n]: an array of strings that represent the rows of the grid
# int startX: starting X coordinate
# int startY: starting Y coordinate
# int goalX: ending X coordinate
# int goalY: ending Y coordinate
# Returns

# int: the minimum moves to reach the goal
# Input Format

# The first line contains an integer , the size of the array grid.
# Each of the next  lines contains a string of length .
# The last line contains four space-separated integers, 

# Constraints

# Sample Input

# STDIN       FUNCTION
# -----       --------
# 3           grid[] size n = 3
# .X.         grid = ['.X.','.X.', '...']
# .X.
# ...
# 0 0 0 2     startX = 0, startY = 0, goalX = 0, goalY = 2
# Sample Output

# 3
# Explanation

# Here is a path that one could follow in order to reach the destination in  steps:

# .

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

def minimumMoves(grid, startX, startY, goalX, goalY):
    # Write your code here
    queue = []
    n = len(grid)
    ds = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    visited = [[False] * n for _ in range(n)]
    queue.append([startX, startY])
    visited[startX][startY] = True
    step = 0

    while len(queue) > 0:
        length = len(queue)
        step += 1

        for _ in range(length):
            curr = queue.pop(0)

            for d in ds:
                newX = curr[0]
                newY = curr[1]

                while not (newX < 0 or newX >= n or newY < 0 or newY >= n or grid[newX][newY] == 'X'):
                    if newX == goalX and newY == goalY:
                        return step

                    if not visited[newX][newY]:
                        queue.append([newX, newY])
                        visited[newX][newY] = True

                    newX += d[0]
                    newY += d[1]

    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()



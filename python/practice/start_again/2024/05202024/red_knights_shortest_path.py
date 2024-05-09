# #   https://www.hackerrank.com/challenges/red-knights-shortest-path/problem?isFullScreen=true

# In ordinary chess, the pieces are only of two colors, black and white. In our version of chess, we are including new pieces with unique movements. One of the most powerful pieces in this version is the red knight.

# The red knight can move to six different positions based on its current position (UpperLeft, UpperRight, Right, LowerRight, LowerLeft, Left) as shown in the figure below.

# image

# The board is a grid of size . Each cell is identified with a pair of coordinates , where  is the row number and  is the column number, both zero-indexed. Thus,  is the upper-left corner and  is the bottom-right corner.

# Complete the function printShortestPath, which takes as input the grid size , and the coordinates of the starting and ending position  and  respectively, as input. The function does not return anything.

# Given the coordinates of the starting position of the red knight and the coordinates of the destination, print the minimum number of moves that the red knight has to make in order to reach the destination and after that, print the order of the moves that must be followed to reach the destination in the shortest way. If the destination cannot be reached, print only the word "Impossible".

# Note: There may be multiple shortest paths leading to the destination. Hence, assume that the red knight considers its possible neighbor locations in the following order of priority: UL, UR, R, LR, LL, L. In other words, if there are multiple possible options, the red knight prioritizes the first move in this list, as long as the shortest path is still achievable. Check sample input  for an illustration.

# Input Format

# The first line of input contains a single integer . The second line contains four space-separated integers .  denotes the coordinates of the starting position and  denotes the coordinates of the final position.

# Constraints

# the starting and the ending positions are different
# Output Format

# If the destination can be reached, print two lines. In the first line, print a single integer denoting the minimum number of moves that the red knight has to make in order to reach the destination. In the second line, print the space-separated sequence of moves.

# If the destination cannot be reached, print a single line containing only the word Impossible.

# Sample Input 0

# 7
# 6 6 0 1
# Sample Output 0

# 4
# UL UL UL L
# Explanation 0

# image

# Sample Input 1

# 6
# 5 1 0 5
# Sample Output 1

# Impossible
# Explanation 1

# image

# Sample Input 2

# 7
# 0 3 4 3
# Sample Output 2

# 2
# LR LL
# Explanation 2

# image


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'printShortestPath' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER i_start
#  3. INTEGER j_start
#  4. INTEGER i_end
#  5. INTEGER j_end
#

def isvalid(x, y, n, visited):
    if (x, y) in visited:
        return False
        
    if x < 0 or x > n-1 or y < 0 or y > n-1:
        return False
    return True

def printShortestPath(n, i_start, j_start, i_end, j_end):
    # Print the distance along with the sequence of moves.
    moves = [[-2, -1], [-2, 1], [0, 2], [2, 1], [2, -1], [0, -2]]
    mstr = ['UL', 'UR', 'R', 'LR', 'LL', 'L']
    dq = deque()
    dist = [[n*n for i in range(n)] for j in range(n)]
    visited = set()
    path = [[[] for i in range(n)] for j in range(n)]
    
    dq.append((i_start, j_start))
    dist[i_start][j_start] = 0
    visited.add((i_start, j_start))
    while len(dq) > 0:
        i, j = dq.popleft()
        for k in range(len(moves)):
            nexti = i + moves[k][0]
            nextj = j + moves[k][1]
            if isvalid(nexti, nextj, n, visited):
                dq.append((nexti, nextj))
                if dist[nexti][nextj] > dist[i][j] + 1:
                    path[nexti][nextj] = path[i][j] + [mstr[k]]
                    dist[nexti][nextj] = dist[i][j] + 1
                visited.add((nexti, nextj))
                
    if dist[i_end][j_end] >= n*n:
        print('Impossible')
        return
    
    print(dist[i_end][j_end])
    print(' '.join(path[i_end][j_end]))

if __name__ == '__main__':
    n = int(input().strip())

    first_multiple_input = input().rstrip().split()

    i_start = int(first_multiple_input[0])

    j_start = int(first_multiple_input[1])

    i_end = int(first_multiple_input[2])

    j_end = int(first_multiple_input[3])

    printShortestPath(n, i_start, j_start, i_end, j_end)

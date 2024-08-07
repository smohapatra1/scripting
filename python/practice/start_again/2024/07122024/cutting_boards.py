# #   https://www.hackerrank.com/challenges/board-cutting/problem?isFullScreen=true

# Alice gives Bob a board composed of  wooden squares and asks him to find the minimum cost of breaking the board back down into its individual squares. To break the board down, Bob must make cuts along its horizontal and vertical lines.

# To reduce the board to squares, Bob makes horizontal and vertical cuts across the entire board. Each cut has a given cost,  or  for each cut along a row or column across one board, so the cost of a cut must be multiplied by the number of segments it crosses. The cost of cutting the whole board down into  squares is the sum of the costs of each successive cut.

# Can you help Bob find the minimum cost? The number may be large, so print the value modulo .

# For example, you start with a  board. There are two cuts to be made at a cost of  for the horizontal and  for the vertical. Your first cut is across  piece, the whole board. You choose to make the horizontal cut between rows  and  for a cost of . The second cuts are vertical through the two smaller boards created in step  between columns  and . Their cost is . The total cost is  and .

# Function Description

# Complete the boardCutting function in the editor below. It should return an integer.

# boardCutting has the following parameter(s):

# cost_x: an array of integers, the costs of vertical cuts
# cost_y: an array of integers, the costs of horizontal cuts
# Input Format

# The first line contains an integer , the number of queries.

# The following  sets of lines are as follows:

# The first line has two positive space-separated integers  and , the number of rows and columns in the board.
# The second line contains  space-separated integers cost_y[i], the cost of a horizontal cut between rows  and  of one board.
# The third line contains  space-separated integers cost_x[j], the cost of a vertical cut between columns  and  of one board.
# Constraints

# Output Format

# For each of the  queries, find the minimum cost () of cutting the board into  squares and print the value of .

# Sample Input 0

# 1
# 2 2
# 2
# 1
# Sample Output 0

# 4
# Explanation 0
# We have a  board, with cut costs  and . Our first cut is horizontal between  and , because that is the line with the highest cost (). Our second cut is vertical, at . Our first cut has a  of  because we are making a cut with cost  across  segment, the uncut board. The second cut also has a  of  but we are making a cut of cost  across  segments. Our answer is .

# Sample Input 1

# 1
# 6 4
# 2 1 3 1 4
# 4 1 2
# Sample Output 1

# 42
# Explanation 1
# Our sequence of cuts is: , , , , , ,  and .
# Cut 1: Horizontal with cost  across  segment. .
# Cut 2: Vertical with cost  across  segments. .
# Cut 3: Horizontal with cost  across  segments. .
# Cut 4: Horizontal with cost  across  segments. .
# Cut 5: Vertical with cost  across  segments. .
# Cut 6: Horizontal with cost  across  segments. .
# Cut 7: Horizontal with cost  across  segments. .
# Cut 8: Vertical with cost  across  segments. .

# . We then print the value of .

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'boardCutting' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost_y
#  2. INTEGER_ARRAY cost_x
#

def boardCutting(cost_y, cost_x):
    # Write your code here
    MOD = 10**9 + 7 
    all_costs = sorted([(cost, 'h') for cost in cost_y] + [(cost, 'v') for cost in cost_x], reverse=True)
    horizontal_segments = 1 
    vertical_segments = 1 
    total_cost = 0
    for cost, cut_type in all_costs:
        if cut_type == 'h':
            total_cost = (total_cost + cost * vertical_segments ) % MOD
            horizontal_segments +=1
        elif cut_type == 'v':
            total_cost = (total_cost + cost * horizontal_segments ) % MOD
            vertical_segments +=1
    return total_cost
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        m = int(first_multiple_input[0])

        n = int(first_multiple_input[1])

        cost_y = list(map(int, input().rstrip().split()))

        cost_x = list(map(int, input().rstrip().split()))

        result = boardCutting(cost_y, cost_x)

        fptr.write(str(result) + '\n')

    fptr.close()

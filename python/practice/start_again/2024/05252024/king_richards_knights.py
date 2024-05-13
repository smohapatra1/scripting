# #   https://www.hackerrank.com/challenges/king-richards-knights/problem?isFullScreen=true

# King Richard is leading a troop of  knights into battle! Being very organized, he labels his knights  and arranges them in an  square formation, demonstrated below:

# knight1

# Before the battle begins, he wants to test how well his knights follow instructions. He issues  drill commands, where each command follows the format ai bi di and is executed like so:

# All knights in the square having the top-left corner at location  and the bottom-right corner at location  rotate  in the clockwise direction. Recall that some location  denotes the cell located at the intersection of row  and column . For example: image
# You must follow the commands sequentially. The square for each command is completely contained within the square for the previous command. Assume all knights follow the commands perfectly.

# After performing all  drill commands, it's time for battle! King Richard chooses knights  for his first wave of attack; however, because the knights were reordered by the drill commands, he's not sure where his chosen knights are!

# As his second-in-command, you must find the locations of the knights. For each knight , , print the knight's row and column locations as two space-separated values on a new line.

# Input Format

# This is broken down into three parts:

# The first line contains a single integer, .
# The second line contains a single integer, .
# Each line  of the  subsequent lines describes a command in the form of three space-separated integers corresponding to , , and , respectively.
# The next line contains a single integer, .
# Each line  of the  subsequent lines describes a knight the King wants to find in the form of a single integer corresponding to .
# Constraints

#  and 
#  and 
# Subtask

#  for  of the maximum score.
# Output Format

# Print  lines of output, where each line  contains two space-separated integers describing the respective row and column values where knight  is located.

# Sample Input

# 7
# 4
# 1 2 4
# 2 3 3
# 3 4 1
# 3 4 0
# 7
# 0
# 6
# 9
# 11
# 24
# 25
# 48
# Sample Output

# 1 1
# 1 7
# 4 6
# 3 4
# 2 5
# 2 4
# 7 7
# Explanation

# The following diagram demonstrates the sequence of commands:

#  Click here to download a larger image.

# In the final configuration:

# Knight  is at location 
# Knight  is at location 
# Knight  is at location 
# Knight  is at location 
# Knight  is at location 
# Knight  is at location 
# Knight  is at location 


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kingRichardKnights' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER s
#  3. INTEGER_ARRAY knights
#

def identity():
    return [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]

def cw(x, y, k):
    return [
        [1, x - y, k + x + y],
        [0, 0, -1],
        [0, 1, 0],
    ]

def ccw(x, y, k):
    return [
        [1, k + x + y, -x + y],
        [0, 0, 1],
        [0, -1, 0],
    ]


# from profiler import line_profile

def multiply(a, b):
    c = [
        [0] * len(b[0])
        for _ in range(len(a))
    ]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                c[i][j] += a[i][k] * b[k][j]

    return c
# return [
#         a[0][0]*b[0][0] + a[0][1]*b[1][0] + a[0][2] * b[2][0]
#     ]

def multiply_ccw(x, y, k, a):
    return [[
        a[0][i] + (k + x + y) * a[1][i] + (-x + y) * a[2][i]
        for i in range(3)
    ], [
        a[2][i]
        for i in range(3)
    ], [
        -a[1][i]
        for i in range(3)
    ]]

def multiply_cw(x, y, k, a):
    return [[
        a[0][i] + (x - y) * a[1][i] + (k + x + y) * a[2][i]
        for i in range(3)
    ], [
        -a[2][i]
        for i in range(3)
    ], [
        a[1][i]
        for i in range(3)
    ]]
    

def kingRichardKnights(n, s, knights):
    # Write your code here
    new_commands = []

    t = identity()
    for ind, c in enumerate(commands):
        m = multiply([[1, c[0], c[1]]], t)

        new_command = [m[0][1], m[0][2], c[2]]
        if (ind % 4) == 1:
            new_command[0] -= c[2]
        elif (ind % 4) == 2:
            new_command[0] -= c[2]
            new_command[1] -= c[2]
        elif (ind % 4) == 3:
            new_command[1] -= c[2]
        new_commands.append(new_command)

        # t = multiply(ccw(c[0], c[1], c[2]), t)
        t = multiply_ccw(c[0], c[1], c[2], t)

    to_process = {}
    for k in knights:
        i, j = (k // n) + 1, (k % n) + 1

        l = -1
        r = len(new_commands)
        while r - l > 1:
            s = (l + r) // 2
            x, y, k = new_commands[s]
            if (x <= i <= x + k and
                    y <= j <= y + k):
                l = s
            else:
                r = s

        to_process.setdefault(l, [])
        to_process[l].append((i, j))

    ans = {
        k: k
        for k in to_process.get(-1, [])
    }

    t = identity()
    for ind, c in enumerate(new_commands):
        # t = multiply(cw(c[0], c[1], c[2]), t)
        t = multiply_cw(c[0], c[1], c[2], t)
        for k in to_process.get(ind, []):
            m = multiply([[1, k[0], k[1]]], t)
            ans[k] = [m[0][1], m[0][2]]

    result = []
    for k in knights:
        result.append(ans[(k // n) + 1, (k % n) + 1])

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = int(input().strip())

    commands = []

    for _ in range(s):
        commands.append(list(map(int, input().rstrip().split())))

    knights_count = int(input().strip())

    knights = []

    for _ in range(knights_count):
        knights_item = int(input().strip())
        knights.append(knights_item)

    result = kingRichardKnights(n, s, knights)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()

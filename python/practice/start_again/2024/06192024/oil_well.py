# #   https://www.hackerrank.com/challenges/oil-well/problem?isFullScreen=true

# Mr. Road Runner bought a piece of land in the middle of a desert for a nominal amount. It turns out that the piece of land is now worth millions of dollars as it has an oil reserve under it. Mr. Road Runner contacts the ACME corp to set up the oil wells on his land. Setting up oil wells is a costly affair and the charges of setting up oil wells are as follows.

# The rectangular plot bought by Mr. Road Runner is divided into r * c blocks. Only some blocks are suitable for setting up the oil well and these blocks have been marked. ACME charges nothing for building the first oil well. For every subsequent oil well built, the cost would be the maximum ACME distance between the new oil well and the existing oil wells.

# If (x,y) is the position of the block where a new oil well is setup and (x1, y1) is the position of the block of an existing oil well, the ACME distance is given by

# max(|x-x1|, |y-y1|)
# the maximum ACME distance is the maximum among all the ACME distance between existing oil wells and new wells.

# If the distance of any two adjacent blocks (horizontal or vertical) is considered 1 unit, what is the minimum cost (E) in units it takes to set up oil wells across all the marked blocks?

# Input Format

# The first line of the input contains two space separated integers r *c*.
# r lines follow each containing c space separated integers.
# 1 indicates that the block is suitable for setting up an oil well, whereas 0 isn't.

# r c  
# M11 M12 ... M1c  
# M21 M22 ... M2c  
# ...  
# Mr1 Mr2 ... Mrc  
# Constraints

# 1 <= r, c <= 50
# Output Format

# Print the minimum value E as the answer.

# Sample Input

# 3 4
# 1 0 0 0
# 1 0 0 0
# 0 0 1 0
# Sample Output

# 3  
# Explanation

# (1, 1) (2, 1) (3, 3) are the places where are to be setup.
# There are 3! = 6 ways to do it.

# (1, 1) (2, 1) (3, 3) ==> cost = 0 + 1 + 2 = 3
# (1, 1) (3, 3) (2, 1) ==> cost = 0 + 2 + 2 = 4
# (2, 1) (1, 1) (3, 3) ==> cost = 0 + 1 + 2 = 3
# (2, 1) (3, 3) (1, 1) ==> cost = 0 + 2 + 2 = 4
# (3, 3) (1, 1) (2, 1) ==> cost = 0 + 2 + 2 = 4
# (3, 3) (2, 1) (1, 1) ==> cost = 0 + 2 + 2 = 4

# So E = 3

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'oilWell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY blocks as parameter.
#

r, c = map(int, input().strip().split())
n = max(r, c)
g = [[0] * n for i in range(n)]
for i in range(r):
    bs = list(map(int, input().strip().split()))
    for j in range(c):
        g[i][j] = bs[j]
x = [[0] * (n + 1) for i in range(n + 1)]
for i in range(n):
    for j in range(n):
        x[i + 1][j + 1] = x[i + 1][j] + x[i][j + 1] - x[i][j] + g[i][j]
fs  = g
fz  = [[0] * n for i in range(n)]
ans = [[0] * n for i in range(n)]
anz = [[0] * n for i in range(n)]
for d in range(1, n):
    for i in range(n - d):
        I = i + d + 1
        for j in range(n-d):
            J = j + d + 1
            total = fz[i][j] = x[I][J] - x[i][J] - x[I][j] + x[i][j]
            anz[i][j] = min(
                ans[i][j] + d * (total - fs[i][j]),
                ans[i][j + 1] + d * (total - fs[i][j + 1]),
                ans[i + 1][j] + d * (total - fs[i + 1][j]),
                ans[i + 1][j + 1] + d*(total - fs[i + 1][j + 1]))
    ans, anz = anz, ans
    fs, fz =  fz, fs
print(ans[0][0])


# def oilWell(blocks):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     r = int(first_multiple_input[0])

#     c = int(first_multiple_input[1])

#     blocks = []

#     for _ in range(r):
#         blocks.append(list(map(int, input().rstrip().split())))

#     result = oilWell(blocks)

#     fptr.write(str(result) + '\n')

#     fptr.close()

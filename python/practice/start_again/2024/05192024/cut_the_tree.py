# #   https://www.hackerrank.com/challenges/cut-the-tree/problem?isFullScreen=true

# There is an undirected tree where each vertex is numbered from  to , and each contains a data value. The sum of a tree is the sum of all its nodes' data values. If an edge is cut, two smaller trees are formed. The difference between two trees is the absolute value of the difference in their sums.

# Given a tree, determine which edge to cut so that the resulting trees have a minimal difference between them, then return that difference.

# Example


# In this case, node numbers match their weights for convenience. The graph is shown below.

# image

# The values are calculated as follows:

# Edge    Tree 1  Tree 2  Absolute
# Cut     Sum      Sum     Difference
# 1        8         13         5
# 2        9         12         3
# 3        6         15         9
# 4        4         17        13
# 5        5         16        11
# The minimum absolute difference is .

# Note: The given tree is always rooted at vertex .

# Function Description

# Complete the cutTheTree function in the editor below.

# cutTheTree has the following parameter(s):

# int data[n]: an array of integers that represent node values
# int edges[n-1][2]: an 2 dimensional array of integer pairs where each pair represents nodes connected by the edge
# Returns

# int: the minimum achievable absolute difference of tree sums
# Input Format

# The first line contains an integer , the number of vertices in the tree.
# The second line contains  space-separated integers, where each integer  denotes the  data value, .
# Each of the  subsequent lines contains two space-separated integers  and  that describe edge  in tree .

# Constraints

# , where .
# Sample Input

# STDIN                       Function
# -----                       --------
# 6                           data[] size n = 6
# 100 200 100 500 100 600     data = [100, 200, 100, 500, 100, 600]
# 1 2                         edges = [[1, 2], [2, 3], [2, 5], [4, 5], [5, 6]]
# 2 3
# 2 5
# 4 5
# 5 6
# Sample Output

# 400
# Explanation

# We can visualize the initial, uncut tree as:

# cut-the-tree.png

# There are  edges we can cut:

# Edge  results in 
# Edge  results in 
# Edge  results in 
# Edge  results in 
# Edge  results in 
# The minimum difference is .


#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(10**5)

#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#

def dfs(conn , node, sums, data, parent):
    if sums[node]!=0:
        return sums[node]
    nb = conn[node]
    if len(nb)==1 and node!=0:
        sums[node] = data[node]
        return data[node]
    ans = 0
    for n1 in nb:
        if n1!=parent:
            ans += dfs(conn, n1, sums, data, node)
    ans += data[node]
    sums[node] = ans 
    return ans

def cutTheTree(data, edges):
    # Write your code here
    conn = [[] for i in range(n)]
    for e in edges:
        e1 = e[0]-1
        e2 = e[1]-1
        conn[e1].append(e2)
        conn[e2].append(e1)
    sums = [0 for i in range(n)]
    dfs(conn , 0, sums, data, 0)
    print(sums)
    mindiff = 999999999
    for i in range(1, n):
        ## seperate node i
        sum1 = sums[i]
        sum2 = sums[0] - sums[i]
        diff = abs(sum1 - sum2)
        mindiff = min(mindiff, diff)
    return mindiff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    fptr.write(str(result) + '\n')

    fptr.close()

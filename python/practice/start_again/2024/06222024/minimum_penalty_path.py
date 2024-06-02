# #   https://www.hackerrank.com/challenges/beautiful-path/problem?isFullScreen=true

# Consider an undirected graph containing  nodes and  edges. Each edge  has an integer cost, , associated with it.

# The penalty of a path is the bitwise OR of every edge cost in the path between a pair of nodes,  and . In other words, if a path contains edges , then the penalty for this path is  OR  OR ... OR .

# Given a graph and two nodes,  and , find the path between  and  having the minimal possible penalty and print its penalty; if no such path exists, print  to indicate that there is no path from  to .

# Note: Loops and multiple edges are allowed. The bitwise OR operation is known as or in Pascal and as | in C++ and Java.

# Input Format

# The first line contains two space-separated integers,  (the number of nodes) and  (the number of edges), respectively.

# Each line  of the  subsequent lines contains three space-separated integers , , and , respectively, describing edge  connecting the nodes  and  and its associated penalty ().

# The last line contains two space-separated integers,  (the starting node) and  (the ending node), respectively.

# Constraints

# Output Format

# Print the minimal penalty for the optimal path from node  to node ; if no path exists from node  to node , print .

# Sample Input

# 3 4
# 1 2 1
# 1 2 1000
# 2 3 3
# 1 3 100
# 1 3
# Sample Output

# 3
# Explanation

# The optimal path is .
#  and .
# The penalty for this path is:  OR , so we print .


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict, deque

#
# Complete the 'beautifulPath' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY edges
#  2. INTEGER A
#  3. INTEGER B
#

def main():
    nvert, nedge = readints()
    edge = [[] for _ in range(nvert)]
    for _ in range(nedge):
        v1, v2, cost = readints()
        edge[v1-1].append((v2-1, cost))
        edge[v2-1].append((v1-1, cost))
    start, fin = readints()
    print(bestcost(edge, start-1, fin-1))

def readints():
    return [int(fld) for fld in input().split()]

def bestcost(edge, start, fin):
    if not canreach(edge, start, fin, 0):
        return -1
    ans = 0
    forbid = 0
    curbit = 512
    while curbit:
        if canreach(edge, start, fin, forbid|curbit):
            forbid |= curbit
        else:
            ans |= curbit
        curbit >>= 1
    return ans

def canreach(edge, start, fin, forbid):
    seen = [False] * len(edge)
    stack = [start]
    while stack:
        v = stack.pop()
        if v == fin:
            return True
        if not seen[v]:
            seen[v] = True
            stack += [v2 for v2, cost in edge[v] if cost&forbid == 0]
    return False
    
main()
        

# def beautifulPath(edges, A, B):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     m = int(first_multiple_input[1])

#     edges = []

#     for _ in range(m):
#         edges.append(list(map(int, input().rstrip().split())))

#     second_multiple_input = input().rstrip().split()

#     A = int(second_multiple_input[0])

#     B = int(second_multiple_input[1])

#     result = beautifulPath(edges, A, B)

#     fptr.write(str(result) + '\n')

#     fptr.close()

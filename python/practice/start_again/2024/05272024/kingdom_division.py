# #   https://www.hackerrank.com/challenges/kingdom-division/problem?isFullScreen=true

# King Arthur has a large kingdom that can be represented as a tree, where nodes correspond to cities and edges correspond to the roads between cities. The kingdom has a total of  cities numbered from  to .

# The King wants to divide his kingdom between his two children, Reggie and Betty, by giving each of them  or more cities; however, they don't get along so he must divide the kingdom in such a way that they will not invade each other's cities. The first sibling will invade the second sibling's city if the second sibling has no other cities directly connected to it. For example, consider the kingdom configurations below:

# image

# Given a map of the kingdom's  cities, find and print the number of ways King Arthur can divide it between his two children such that they will not invade each other. As this answer can be quite large, it must be modulo .

# Input Format

# The first line contains a single integer denoting  (the number of cities in the kingdom).
# Each of the  subsequent lines contains two space-separated integers,  and , describing a road connecting cities  and .

# Constraints

# It is guaranteed that all cities are connected.
# Subtasks

#  for  of the maximum score.
# Output Format

# Print the number of ways to divide the kingdom such that the siblings will not invade each other, modulo .

# Sample Input

# 5
# 1 2
# 1 3
# 3 4
# 3 5
# Sample Output

# 4
# Explanation

# In the diagrams below, red cities are ruled by Betty and blue cities are ruled by Reggie. The diagram below shows a division of the kingdom that results in war between the siblings:

# image

# Because cities  and  are not connected to any other red cities, blue city  will cut off their supplies and declare war on them. That said, there are four valid ways to divide the kingdom peacefully:

# image

# We then print the value of  as our answer.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kingdomDivision' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY roads
#

def countColorings(root):
    v = {}
    for depth, node in d:
        if len(t[node]) == 0:
            v[(node, True)] = 1
            v[(node, False)] = 0
        else:
            cases = 1
            invalid = 1
            for child in t[node]:
                cases *= v[(child, True)] + v[(child, False)]
                invalid *= v[(child, False)]
            v[(node, True)] = cases
            v[(node, False)] = cases - invalid
    return v[(root, False)] * 2


def spanningTree(root):
    stack = [(root, 0)]
    while stack:
        node, depth = stack.pop()
        t[node] = set()
        d.append((depth, node))
        for adj in g[node]:
            if adj not in t:
                t[node].add(adj)
                stack.append((adj, depth + 1))

def kingdomDivision(n, roads):
    # Write your code here
    global g
    g = {}
    for road in roads:
        if road[0] in g:
            g[road[0]].add(road[1])
        else:
            g[road[0]] = {road[1]}
        if road[1] in g:
            g[road[1]].add(road[0])
        else:
            g[road[1]] = {road[0]}
    global t
    t = {}
    global d
    d = []
    spanningTree(n // 2)
    d.sort(reverse=True)
    return countColorings(n // 2) % (10 ** 9 + 7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    result = kingdomDivision(n, roads)

    fptr.write(str(result) + '\n')

    fptr.close()

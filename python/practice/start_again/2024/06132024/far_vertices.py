# #   https://www.hackerrank.com/challenges/far-vertices/problem?isFullScreen=true

# You are given a tree that has N vertices and N-1 edges. Your task is to mark as small number of vertices as possible, such that, the maximum distance between two unmarked vertices is less than or equal to K. Output this value. Distance between two vertices i and j is defined as the minimum number of edges you have to pass in order to reach vertex i from vertex j.

# Input Format
# The first line of input contains two integers N and K. The next N-1 lines contain two integers (ui,vi) each, where 1 <= ui,vi <= N. Each of these lines specifies an edge.
# N is no more than 100. K is less than N.

# Output Format
# Print an integer that denotes the result of the test.

# Sample Input:

# 5 1  
# 1 2  
# 1 3  
# 1 4  
# 1 5
# Sample Output:

# 3
# Sample Input:

# 5 2  
# 1 2  
# 1 3  
# 1 4  
# 1 5
# Sample Output:

# 0
# Explanation:

# In the first case you have to mark at least 3 vertices, and in the second case you don't need to mark any vertices.



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'farVertices' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. 2D_INTEGER_ARRAY edges
#

n, k = [int(a) for a in input().split(" ")]
count = 0

class Node(object):
    def __init__(self):
        self.neighbors = []
        self.marked = False

    def set_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def mark_dfs(self, depth, root = False):
        global count
        self.marked = True
        count += 1
        if depth == 0:
            children = len(self.neighbors) - 1
            if not root:
                return children
            return min(children, 1)
        num_children = 0
        for neighbor in self.neighbors:
            if not neighbor.marked:
                mc = neighbor.mark_dfs(depth-1)
                if root:
                    num_children = max(num_children,mc)
                else:
                    num_children += mc
        return num_children

nodes = []
for i in range(n):
    node = Node()
    nodes.append(node)

def unmark_all():
    for node in nodes:
        node.marked = False

for i in range(n - 1):
    u, v = [int(a) - 1 for a in input().split(" ")]
    nodes[u].set_neighbor(nodes[v])
    nodes[v].set_neighbor(nodes[u])
max_count = 0
for node in nodes:
    c = node.mark_dfs(k // 2, True)
    if k % 2 == 1:
        count += c
    if count > max_count:
        max_count = count
    unmark_all()
    count = 0  
print(n - max_count)


# def farVertices(n, k, edges):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     k = int(first_multiple_input[1])

#     edges = []

#     for _ in range(n - 1):
#         edges.append(list(map(int, input().rstrip().split())))

#     result = farVertices(n, k, edges)

#     fptr.write(str(result) + '\n')

#     fptr.close()

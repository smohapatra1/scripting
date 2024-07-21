# #   https://www.hackerrank.com/challenges/diameter-minimization/problem?isFullScreen=true

# We define the diameter of a strongly-connected oriented graph, , as the minimum integer  such that for each  there is a path from  to  of length  (recall that a path's length is its number of edges).

# Given two integers,  and , build a strongly-connected oriented graph with  vertices where each vertex has outdegree  and the graph's diameter is as small as possible (see the Scoring section below for more detail). Then print the graph according to the Output Format specified below.

# Here's a sample strongly-connected oriented graph with  nodes, whose outdegree is  and diameter is .

# image

# Note: Cycles and multiple edges between vertices are allowed.

# Input Format

# Two space-separated integers describing the respective values of  (the number of vertices) and  (the outdegree of each vertex).

# Constraints

# Scoring

# We denote the diameter of your graph as  and the diameter of the graph in the author's solution as . Your score for each test case (as a real number from  to ) is:

#  if 
#  if 
#  if 
# Output Format

# First, print an integer denoting the diameter of your graph on a new line.
# Next, print  lines where each line  () contains  space-separated integers in the inclusive range from  to  describing the endpoints for each of vertex 's outbound edges.

# Sample Input 0

# 5 2
# Sample Output 0

# 2
# 1 4
# 2 0
# 3 1
# 4 2
# 0 3
# Explanation 0

# The diagram below depicts a strongly-connected oriented graph with  nodes where each node has an outdegree of :



# The diameter of this graph is , which is minimal as the outdegree of each node must be . We cannot construct a graph with a smaller diameter of  because it requires an outbound edge from each vertex to each other vertex in the graph (so the outdegree of that graph would be ).


#!/bin/python3

import math
import os
import random
import re
import sys


def opt_diameter(n, m):
    count = 1
    depth = 0
    while count < n:
        depth += 1
        count = m ** depth
    return depth
    
def diameter(n, m):
    count = 1
    depth = 0
    while count < n:
        depth += 1
        count += m ** depth
    left_over = m ** depth - (count - n)
    limit = m ** (depth - 1)
    discount = 1
    if left_over > limit:
        discount = 0
    return max(depth, 2 * depth - discount)

def solve(in_file, out_file):
    n, m = (int(raw) for raw in in_file.readline().strip().split(' '))
    out_file.write("{}\n".format(opt_diameter(n, m)))
    count = 0
    for _ in range(n):
        ret = []
        for _ in range(m):
            val = count % n
            count += 1
            ret.append(str(val))
        out_file.write("{}\n".format(" ".join(ret)))

if __name__ == '__main__':
    from_file = False
    if from_file:
        path = 'Data\\'
        name = 'mega_prime'
        file_input = open(path + name + '.in', 'r')
        file_output = open(path + name + '.out','w')
        solve(file_input, file_output)
        file_input.close()
        file_output.close()
    else:
        solve(sys.stdin, sys.stdout)
        

# if __name__ == '__main__':
#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     m = int(first_multiple_input[1])

#     # Write your code here

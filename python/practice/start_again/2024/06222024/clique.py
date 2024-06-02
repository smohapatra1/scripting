# #   https://www.hackerrank.com/challenges/clique/problem?isFullScreen=true

# A clique in a graph is set of nodes such that there is an edge between any two distinct nodes in the set. Finding the largest clique in a graph is a computationally difficult problem. Currently no polynomial time algorithm is known for solving this. However, you wonder what is the minimum size of the largest clique in any graph with  nodes and  edges.

# For example, consider a graph with  nodes and  edges. The graph below shows  nodes with  edges and no cliques. It is evident that the addition of any  edge must create two cliques with  members each.

# image

# Input Format

# The first line contains an integer , the number of test cases.

# Each of the next  lines contains two space-separated integers  and .

# Constraints

# Output Format

# For each test case, print the minimum size of the largest clique that must be formed given  and .

# Sample Input

# 3  
# 3 2  
# 4 6  
# 5 7
# Sample Output

# 2  
# 4  
# 3
# Explanation

# For the first case, we have two cliques with two nodes each:

# image

# For the second test case, the only valid graph having  nodes and  edges is one where each pair of nodes is connected. So the size of the largest clique cannot be smaller than .

# image

# For the third test case, it is easy to verify that any graph with  nodes and . The  solid lines in the graph below indicate the maximum edges that can be added without forming a clique larger than . The dashed lines could connect any two nodes not connected by solid lines producing a clique of size .

# image
# Hints Turan's theorem gives us an upper bound on the number of edges a graph can have if we wish that it should not have a clique of size . Though the bound is not exact, it is easy to extend the statement of the theorem to get an exact bound in terms of  and . Once this is done, we can binary search for the largest  such that . See: Turan's Theorem


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'clique' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

import math
def s1(n, m):
    ga = n%m
    gb = m-ga
    sa = n//m+1
    sb = n//m
    return ga*gb*sa*sb+ga*(ga-1)*sa*sa//2+gb*(gb-1)*sb*sb//2
def s(n,c):
    l = 1
    h = n+1
    while l+1 < h:
        m = l+(h-l)//2
        k = s1(n,m)
        if k < c:
            l = m
        else:
            h = m
    return h
t = int(input())
for i in range(t):
    n,m=[int(j) for j in input().split()]
    print(s(n,m))

# def clique(n, m):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         first_multiple_input = input().rstrip().split()

#         n = int(first_multiple_input[0])

#         m = int(first_multiple_input[1])

#         result = clique(n, m)

#         fptr.write(str(result) + '\n')

#     fptr.close()

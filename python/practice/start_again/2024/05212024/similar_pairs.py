# #   https://www.hackerrank.com/challenges/similarpair/problem?isFullScreen=true


# A pair of nodes, , is a similar pair if the following conditions are true:

# node  is the ancestor of node 
# Given a tree where each node is labeled from  to , find the number of similar pairs in the tree.

# For example, given the following tree:

# image

# We have the following pairs of ancestors and dependents:

# Pair	abs(a-b)	Pair	abs(a-b)
# 1,2	1		3,4	1
# 1,3	2		3,5	2
# 1,4	3		3,6	3
# 1,5	4
# 1,6	5
# If  for example, we have  pairs that are similar, where .

# Function Description

# Complete the similarPair function in the editor below. It should return an integer that represents the number of pairs meeting the criteria.

# similarPair has the following parameter(s):

# n: an integer that represents the number of nodes
# k: an integer
# edges: a two dimensional array where each element consists of two integers that represent connected node numbers
# Input Format

# The first line contains two space-separated integers  and , the number of nodes and the similarity threshold.
# Each of the next  lines contains two space-separated integers defining an edge connecting nodes  and , where node  is the parent to node .

# Constraints

# Output Format

# Print a single integer denoting the number of similar pairs in the tree.

# Sample Input

# 5 2
# 3 2
# 3 1
# 1 4
# 1 5
# Sample Output

# 4
# Explanation

# image
# The similar pairs are , , , and , so we print  as our answer.
# Observe that  and  are not similar pairs because they do not satisfy  for .


#!/bin/python3

import math
import os
import random
import re
import sys
import resource


#
# Complete the 'similarPair' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. 2D_INTEGER_ARRAY edges
#

sys.setrecursionlimit(2000000)
#resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))
def add(x, v):
    x += 1
    while x <= n:
        a[x] += v
        x += x & -x

def que(x):
    x += 1
    if x <= 0:
        return 0
    ret = 0
    x = min(n, x)
    while x > 0:
        ret += a[x]
        x -= x & -x
    return ret

st = []
vis = {}
def dfs(x):
    
    global ans
    st.append(x)
    while st:
        x = st[-1]
        if not x in vis:
            ans += que(x + T) - que(x - T - 1)
            add(x, 1)
            vis[x] = 1
        if nx[x]:
            st.append(nx[x][-1])
            nx[x].pop()
        else:
            st.pop()
            add(x, -1)

n, T = (int(x) for x in input().split())
a = [0 for i in range(4 * n)]
nx = [[] for i in range(n)]
pre = [-1 for i in range(n)]
for i in range(n - 1):
    s, e = (int(x) - 1 for x in input().split())
    nx[s].append(e)
    pre[e] = s
    
s = 1
while pre[s] != -1:
    s = pre[s]
ans = 0
dfs(s)
print(ans)


# def similarPair(n, k, edges):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     k = int(first_multiple_input[1])

#     edges = []

#     for _ in range(n - 1):
#         edges.append(list(map(int, input().rstrip().split())))

#     result = similarPair(n, k, edges)

#     fptr.write(str(result) + '\n')

#     fptr.close()

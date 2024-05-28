# #   https://www.hackerrank.com/challenges/tree-pruning/problem?isFullScreen=true

# A tree, , has  vertices numbered from  to  and is rooted at vertex . Each vertex  has an integer weight, , associated with it, and 's total weight is the sum of the weights of its nodes. A single remove operation removes the subtree rooted at some arbitrary vertex  from tree .

# Given , perform up to  remove operations so that the total weight of the remaining vertices in  is maximal. Then print 's maximal total weight on a new line.

# Note: If 's total weight is already maximal, you may opt to remove  nodes.

# Input Format

# The first line contains two space-separated integers,  and , respectively.
# The second line contains  space-separated integers describing the respective weights for each node in the tree, where the  integer is the weight of the  vertex.
# Each of the  subsequent lines contains a pair of space-separated integers,  and , describing an edge connecting vertex  to vertex .

# Constraints

# Output Format

# Print a single integer denoting the largest total weight of 's remaining vertices.

# Sample Input

# 5 2
# 1 1 -1 -1 -1
# 1 2
# 2 3
# 4 1
# 4 5
# Sample Output

# 2
# Explanation

# We perform  remove operations:

# Remove the subtree rooted at node . Losing this subtree's  weight increases the tree's total weight by .
# Remove the subtree rooted at node . Losing this subtree's  weight increases the tree's total weight by .
# The sum of our remaining positively-weighted nodes is , so we print  on a new line.



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'treePrunning' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY weights
#  3. 2D_INTEGER_ARRAY tree
#
from collections import defaultdict

INF = -(1e15)

def dfs(x, f, g, k, weights):
    dpc = [INF]*(k+1)
    dpc[0] = weights[x]
    
    for n in g[x]:
        if n == f:
            continue
        dpn = dfs(n, x, g, k, weights)
        dptmp = [INF]*(k+1)
        for i in range(k+1):
            if dpc[i] == INF:
                break
            for j in range(0, k-i+1):
                if dpn[j] == INF:
                    break
                dptmp[i+j] = max(dptmp[i+j], dpc[i]+dpn[j])
            if i+1 <= k:
                dptmp[i+1] = max(dptmp[i+1], dpc[i])
        dpc = dptmp
    return dpc

def treePrunning(k, weights, tree):
    # Write your code here
    g = defaultdict(list)
    for u, v in tree:
        g[u-1].append(v-1)
        g[v-1].append(u-1)

    dpn = dfs(0, -1, g, k, weights)
    return max(max(dpn),0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    weights = list(map(int, input().rstrip().split()))

    tree = []

    for _ in range(n - 1):
        tree.append(list(map(int, input().rstrip().split())))

    result = treePrunning(k, weights, tree)

    fptr.write(str(result) + '\n')

    fptr.close()

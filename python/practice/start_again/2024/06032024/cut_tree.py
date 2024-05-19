# #   https://www.hackerrank.com/challenges/cuttree/problem?isFullScreen=true

# Given a tree T with n nodes, how many subtrees (T') of T have at most K edges connected to (T - T')?

# Input Format

# The first line contains two integers n and K followed by n-1 lines each containing two integers a & b denoting that there's an edge between a & b.

# Constraints

# 1 <= K <= n <= 50
# Every node is indicated by a distinct number from 1 to n.

# Output Format

# A single integer which denotes the number of possible subtrees.

# Sample Input

# 3 1
# 2 1
# 2 3
# Sample Output

# 6
# Explanation

# There are 2^3 possible sub-trees:

# {} {1} {2} {3} {1, 2} {1, 3} {2, 3} {1, 2, 3}

# But:
# the sub-trees {2} and {1,3} are not valid. {2} isn't valid because it has 2 edges connecting to it's complement {1,3} whereas K = 1 in the sample test-case {1,3} isn't valid because, well, it's not a sub-tree. The nodes aren't connected.


#!/bin/python3

import os
import sys
from collections import defaultdict

#
# Complete the cuttree function below.
#
def cutTree(n, k, edges):
    #
    # Write your code here.
    #
    g = [[] for _ in range(n)]
    for i in edges:
        g[i[0]-1].append(i[1]-1)
        g[i[1]-1].append(i[0]-1)
    global ans
    ans = 1
    def multiply(x, y):
        ans = defaultdict(lambda: 0)
        for k, v in x.items():
            for k1, v1 in y.items(): ans[k+k1-1] += v*v1
        for k, v in ans.items():
            if k in x: x[k] += v
            else: x[k] = v
    def dfs(i,p):
        global ans
        if g[i] == [p]:
            ans += 1
            return {0:1}
        x = 1 if i else 0
        res = {len(g[i])-x : 1}
        for nxt in g[i]:
            if nxt != p: multiply(res, dfs(nxt, i))
        ans += sum(((v if i+x <= k else 0) for i, v in res.items()))
        return res
    dfs(0,-1)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    edges = []

    for _ in range(n-1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTree(n, k, edges)

    fptr.write(str(result) + '\n')

    fptr.close()

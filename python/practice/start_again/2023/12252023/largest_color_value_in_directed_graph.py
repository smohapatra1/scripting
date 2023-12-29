# #   https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

# 1857. Largest Color Value in a Directed Graph
# Hard
# 2K
# 67
# Companies
# There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

# You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

# A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

# Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

 

# Example 1:



# Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
# Output: 3
# Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
# Example 2:



# Input: colors = "a", edges = [[0,0]]
# Output: -1
# Explanation: There is a cycle from 0 to 0.

from typing import List
from collections import defaultdict
def LargeColor(colors: str, edges: List[List[int]]) -> int:
    n=len(colors)
    graph=defaultdict(list)
    count=defaultdict(int)
    for u, v in edges:
        graph[u].append(v)
        count[v]+=1
    queue=[]
    dp=[[0] * 26 for _ in range(n)]
    colvalues=[ord(c)-ord("a") for c in colors]
    for u in range(n):
        if u not in count:
            queue.append(u)
            dp[u][colvalues[u]]=1
    visited=0
    while queue:
        u=queue.pop()
        visited+=1
        for v in graph[u]:
            for c in range(26):
                dp[v][c]=max(dp[v][c], dp[u][c] + (c==colvalues[v]))
            count[v]-=1
            if count[v]==0:
                queue.append(v)
                del count[v]
    if visited < n:
        return -1
    return max(max(x) for x in dp)


if __name__ == "__main__":
    colors = "abaca"
    edges = [[0,1],[0,2],[2,3],[3,4]]
    print ("{}".format(LargeColor(colors, edges)))
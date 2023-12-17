# # https://leetcode.com/problems/shortest-path-with-alternating-colors/

# 1129. Shortest Path with Alternating Colors
# Medium
# 3.4K
# 175
# Companies
# You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

# You are given two arrays redEdges and blueEdges where:

# redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
# blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
# Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

 

# Example 1:

# Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
# Output: [0,1,-1]
# Example 2:

# Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
# Output: [0,1,-1]
 
from typing import List
import collections
from collections import defaultdict
def shortestAlternativeColors(n: int, redEdges : List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    d=[defaultdict(list), defaultdict(list)]
    for a,b in redEdges : d[0][a] +=(b,0),
    for a, b in blueEdges: d[1][a] +=(b, 1),
    def dfs(tar):
        q = [(0,0,1) , (0,0,0)]
        seen = [ defaultdict(int), defaultdict(int)]
        for cur, h, p in q:
            if cur == tar: return h
            for n, c in d[1-p][cur]:
                if not seen[1-p][n]:
                    q.append((n, h+1, c))
                    seen [1-p][n] = 1
        return -1
    return  [ i and dfs(i) for i in range(n)]


if __name__ == "__main__":
     n = 3
     redEdges = [[0,1],[1,2]]
     blueEdges = []
     print ("{}".format(shortestAlternativeColors(n, redEdges, blueEdges)))

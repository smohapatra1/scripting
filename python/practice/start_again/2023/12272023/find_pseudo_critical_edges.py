# #   https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/

# 1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
# Hard
# 1.8K
# 148
# Companies
# Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional and weighted edge between nodes ai and bi. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

# Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

# Note that you can return the indices of the edges in any order.

 

# Example 1:



# Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
# Output: [[0,1],[2,3,4,5]]
# Explanation: The figure above describes the graph.
# The following figure shows all the possible MSTs:

# Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.
# The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.
# Example 2:



# Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
# Output: [[],[0,1,2,3]]
# Explanation: We can observe that since all 4 edges have equal weight, choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.
 

from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    def find_parent(self, p):
        if self.parent[p] == p:
            return p
        self.parent[p] = self.find_parent(self.parent[p])
        return self.parent[p]
    def union(self, u, v):
        pu, pv = self.find_parent(u), self.find_parent(v)
        self.parent[pu] = pv
class solutions:
    def FindPseudoCriticalEdge(n: int, edges: List[List[int]]) -> List[List[int]]:
        def cmp(a,b):
            return a[2] < b[2]
        critical = []
        pseudo_critical = []
        for i in range(len(edges)):
            edges[i].append(i)
        edges.sort(key=lambda x: x[2])
        mst_wt = self.find_mst(n, edges , -1, -1 )
        for i in range(len(edges)):
            if mst_wt < self.find_mst(n, edges, i, -1 ):
                critical.append(edges[i][3])
            elif mst_wt == self.find_mst(n, edges, -1, i ):
                pseudo_critical.append(edges[i][3])
        return [ critical, pseudo_critical]
    def find_mst (self, n, edges, block, e ):
        uf = UnionFind(n)
        weight = 0 
        if e != -1:
            weight +=edges[e][2]
            uf.union(edges[e][0], edges[e][1])
        for i in range(len(edges)):
            if i == block:
                continue
            if uf.find_parent(edges[i][0]) == uf.find_parent(edges[i][1]):
                continue
            uf.union(edges[i][0], edges[i][1])
            weight += edges[i][2]
        for i in range(n):
            if uf.find_parent(i) !=uf.find_parent(0):
                return float('inf')
        return weight




    if __name__ == "__main__":
        n = 5
        edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
        print ("{}".format(FindPseudoCriticalEdge(n, edges)))
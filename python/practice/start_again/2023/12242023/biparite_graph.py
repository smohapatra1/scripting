# #   https://leetcode.com/problems/is-graph-bipartite/

# 785. Is Graph Bipartite?
# Medium
# 7.9K
# 357
# Companies
# There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

# There are no self-edges (graph[u] does not contain u).
# There are no parallel edges (graph[u] does not contain duplicate values).
# If v is in graph[u], then u is in graph[v] (the graph is undirected).
# The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

# Return true if and only if it is bipartite.

 

# Example 1:


# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false
# Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
# Example 2:


# Input: graph = [[1,3],[0,2],[1,3],[0,2]]
# Output: true
# Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
 
from typing import List
def isBipartite( graph: List[list[int]]) -> bool:
    n=len(graph)
    colors =[0] * n 
    for i in range(n):
        if colors[i] == 0:
            if not self.dfs(graph, colors, i, 1):
                return False
    return True
def dfs(self, graph, colors, node, color):
    if colors [node] != 0:
        return colors[node] == color
    colors[node] = color
    for neighbor in graph[node]:
        if not self.dfs(graph, colors, neighbor, -color):
            return False
    return True

if __name__ == "__main__":
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    print ("{}".format(isBipartite(graph)))


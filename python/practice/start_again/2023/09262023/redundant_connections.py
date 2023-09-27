# 684. Redundant Connection
# Medium
# 5.8K
# 367
# Companies
# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

# Example 1:


# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
# Example 2:


# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]

from typing import List
def redundant_connection(edges: List[List[int]]) -> List[int]:
    parent={v:-1 for v in range(1, len(edges)+1)}
    def find(u):
        if parent[u] != -1:
            parent[u] = find(parent[u])
            return parent[u]
        else:
            return u 
    def union(u,v):
        parent_of_u=find[u]
        parent_of_v=find(v)
        if parent_of_u == parent_of_v:
            return True
        else:
            parent[parent_of_u] = parent_of_v
            return False
    redundant=None
    for u, v in edges:
        if union(u, v):
            redundant=[u,v]
            return redundant
if __name__ == "__main__":
    edges = [[1,2],[1,3],[2,3]]
    print ("{}".format(redundant_connection(edges)))

# #   
# Description

# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

# Sample I/O

# Example 1

# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

#      0          3
#      |          |
#      1 --- 2    4 

# Output: 2
# Example 2

# Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

#      0           4
#      |           |
#      1 --- 2 --- 3

# Output:  1
# Note

# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
# Methodology

# Start from index 0 to n. For each index, use BFS to find all it’s related numbers and append them to the visited set, if this index has no more related number then count + 1 and start from next index, note that if the index is in visited set. we skip to next index.


from typing import List
from collections import defaultdict
from collections import deque
def countComponents(n:int, edges: List[List[int]]) -> int:
    ans=0
    graph=[[] for _ in range(n)]
    seen = set()
    for u, v in edges:
         graph[u].append(v)
         graph[v].append(u)
    def bfs(node: int, seen : Set[int]) -> None:
         q=collections.deque([node])
         seen.add(node)
         while q:
              u = q.pop()
              for v in graph[u]:
                   if v not in seen:
                        q.append(v)
                        seen.add(v)
    for i in range(n):
        if i not in seen:
            bfs(i, seen)
            ans+=1
    return ans
              

                   


if __name__ == "__main__":
     n = 5
     edges = [[0, 1], [1, 2], [3, 4]]
     print ("{}".format(countComponents(n, edges)))






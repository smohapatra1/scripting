# #   https://leetcode.com/problems/path-with-maximum-probability/

# 1514. Path with Maximum Probability
# Medium
# 3K
# 67
# Companies
# You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

# Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

# If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

 

# Example 1:



# Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
# Output: 0.25000
# Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
# Example 2:



# Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
# Output: 0.30000
# Example 3:



# Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
# Output: 0.00000
# Explanation: There is no path between 0 and 2.
 

from typing import List
from heapq import heappop , heappush
def FindMaxProbability(n: int, edges : List[List[int]], succProb: List[int], start: int, end: int) -> float:
    graph=dict()
    prob=dict()
    for i, (u, v) in enumerate(edges):
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)
        prob[u,v] = prob[v,u] = succProb[i]
    h = [(-1, start)]
    seen = set()
    while h:
        p, n =heappop(h)
        if n == end :
            return -p
        seen.add(n)
        for nn in graph.get(n, []):
            if nn in seen:
                continue
            heappush(h, (p * prob.get((n, nn), 0), nn))
    return 0

if __name__ == "__main__":
    n = 3
    edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.2]
    start = 0
    end = 2
    print ("{}".format(FindMaxProbability(n, edges, succProb, start, end)))

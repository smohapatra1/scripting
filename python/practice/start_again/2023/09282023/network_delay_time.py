# #   https://leetcode.com/problems/network-delay-time/

# 743. Network Delay Time
# Medium
# 6.9K
# 346
# Companies
# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

# Example 1:


# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
# Example 2:

# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1
# Example 3:

# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1

from typing import List 
from collections import defaultdict
import heapq
def Netdelay(times: List[List[int]], n: int, k: int) -> int:
    adj_list=defaultdict(list)
    for x, y, w in times:
        adj_list[x].append((w,y))
    visited=set()
    heap=[(0, k )]
    while heap:
        travel_time, node=heapq.heappop(heap)
        visited.add(node)
        if len(visited) ==n:
            return travel_time
        for time, adjacent_node in adj_list[node]:
            if adjacent_node not in visited:
                heapq.heappush(heap, (travel_time+time, adjacent_node))
    return -1

if __name__ == "__main__":
    # times = [[2,1,1],[2,3,1],[3,4,1]]
    # n = 4
    # k = 2
    times = [[1,2,1]]
    n = 2
    k = 1
    print ("{}".format(Netdelay(times, n, k)))



 
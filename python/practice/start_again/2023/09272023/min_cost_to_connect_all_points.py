# #    https://leetcode.com/problems/min-cost-to-connect-all-points/
# 1584. Min Cost to Connect All Points
# Medium
# 4.7K
# 110
# Companies
# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

# Example 1:


# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation: 

# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.
# Example 2:

# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18


from typing import List
from collections import defaultdict
import collections
import heapq
from heapq import heappush, heappushpop, heapify,  heappop
def Min_cost(points: List[List[int]]) -> List[int]:
    manhattan=lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
    n = len(points)
    c=collections.defaultdict(list)
    for i in range(n):
        for j in range(i+1, n ):
            d=manhattan(points[i], points[j])
            c[i].append((d, j))
            c[j].append((d, i ))
    cnt=1
    ans=0
    visited=[0]*n
    heap=c[0]
    visited[0]=1
    heapq.heapify(heap)
    while heap:
        d,j = heapq.heappop(heap)
        if not visited[j]:
            visited[j]=1
            cnt=cnt+1
            ans=ans+d
            for record in c[j]:
                heapq.heappush(heap, record)
        if cnt >=n:
            break
    return ans

if __name__ == "__main__":
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    #points = [[3,12],[-2,5],[-4,1]]
    print ("{}".format(Min_cost(points)))
# #   https://leetcode.com/problems/as-far-from-land-as-possible/
# 1162. As Far from Land as Possible
# Medium
# 4.1K
# 107
# Companies
# Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

# The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

 

# Example 1:


# Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
# Output: 2
# Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
# Example 2:


# Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
# Output: 4
# Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
 

from typing import List
import collections
def FarFromLand(grid: List[List[int]])-> int:
    n=len(grid)
    q=collections.deque()
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1 : q.append((i,j))
    if not q or len(q) == n*n :
        return -1
    res = -1
    dirs=[(0,1), (0,-1), (1,0), (-1,0)]
    while q:
        size = len(q)
        res +=1
        while size:
            size -=1
            x, y = q.popleft()
            for dx, dy in dirs:
                i, j = x+dx, y+dy
                if 0 <=i < n and 0 <=j < n and grid[i][j] == 0:
                    grid[i][j] = 1
                    q.append((i,j))
    return res

    

if __name__ == "__main__":
     grid = [[1,0,1],[0,0,0],[1,0,1]]
     print ("{}".format(FarFromLand(grid)))
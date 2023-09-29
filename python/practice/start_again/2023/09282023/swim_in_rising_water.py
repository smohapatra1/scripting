#   https://leetcode.com/problems/swim-in-rising-water/
# 778. Swim in Rising Water
# Hard
# 3.4K
# 215
# Companies
# You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

# The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

# Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

 

# Example 1:


# Input: grid = [[0,2],[1,3]]
# Output: 3
# Explanation:
# At time 0, you are in grid location (0, 0).
# You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
# You cannot reach point (1, 1) until time 3.
# When the depth of water is 3, we can swim anywhere inside the grid.
# Example 2:


# Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# Output: 16
# Explanation: The final route is shown.
# We need to wait until time 16 so that (0, 0) and (4, 4) are connected.


from typing import List
import heapq
def rise_swim(grid: List[List[int]]) -> int:
    r=len(grid)
    c=len(grid[0])
    vis=[[0]*c for _ in range(r)]
    queue=[(grid[0][0],0,0)]
    heapq.heapify(queue)
    vis[0][0]=1
    while queue:
        rx,x,y=heapq.heappop(queue)
        if x==r-1 and y==c-1:
            return rx
        row=[0,0,-1,1]
        col=[1,-1,0,0]
        for i in range(4):
            if 0<=x+row[i]<r and 0<=y+col[i]<c:
                if vis[x+row[i]][y+col[i]]==0:
                    heapq.heappush(queue,(max(rx,grid[x+row[i]][y+col[i]]),x+row[i],y+col[i]))
                    vis[x+row[i]][y+col[i]]=1

if __name__ == "__main__":
    grid = [[0,2],[1,3]]
    print ("{}".format(rise_swim(grid)))
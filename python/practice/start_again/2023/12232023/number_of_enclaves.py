# #   https://leetcode.com/problems/number-of-enclaves/

# 1020. Number of Enclaves
# Medium
# 3.8K
# 71
# Companies
# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

# Example 1:


# Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
# Example 2:


# Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# Output: 0
# Explanation: All 1s are either on the boundary or can reach the boundary.
 
from typing import List
def NumEnclaves(grid: List[List[int]]) -> int:
    m=len(grid)
    n=len(grid[0])
    def dfs(i, j):
        grid[i][j] = 0
        for x, y in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
            if 0 <= x < m and 0 <= y < n and grid[x][y]:
                dfs(x, y)
    for i in range(m):
        for j in range(n):
            if grid[i][j]== 1 and (i ==0 or j == 0 or i == m-1 or j == n-1):
                dfs(i,j)
    return sum(sum(row) for row in grid)

if __name__ == "__main__":
    grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
    print ("{}".format(NumEnclaves(grid)))
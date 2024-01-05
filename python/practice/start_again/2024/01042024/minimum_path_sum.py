# #   https://leetcode.com/problems/minimum-path-sum/

# 64. Minimum Path Sum
# Medium
# 12K
# 157
# Companies
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

 

# Example 1:


# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# Example 2:

# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
 
from typing import List
def MinPathSum(grid: List[List[int]]) -> int:
    m=len(grid)
    n=len(grid[0])
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    for i in range(1, n):
        grid[0][i] +=grid[0][i-1]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] +=min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]

if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print ("{}".format(MinPathSum(grid)))

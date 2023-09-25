# #   https://leetcode.com/problems/number-of-islands/

# 200. Number of Islands
# Medium
# 21.3K
# 457
# Companies
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

from typing import List
def NumofIsland(grid : List[List[str]]) -> int:
    count=0
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if grid[r][c] == '1' :
                removeNeighbors(r, c, grid)
                count +=1
    return count
def removeNeighbors(r, c, grid):
    grid[r][c] = 0 
    if r+1 < len(grid) and grid[r+1][c] == '1' :
        removeNeighbors(r+1, c, grid)
    if c+1 < len(grid[0]) and grid[r][c+1] == '1':
        removeNeighbors(r, c+1, grid)
    if r -1 >= 0 and grid[r-1][c] == '1':
        removeNeighbors(r-1, c, grid)
    if c-1 >= 0 and grid[r][c-1] == '1':
        removeNeighbors(r, c-1, grid)

if __name__ == "__main__":
    # grid = [
    # ["1","1","1","1","0"],
    # ["1","1","0","1","0"],
    # ["1","1","0","0","0"],
    # ["0","0","0","0","0"]
    # ]
    grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
print ("{}".format(NumofIsland(grid)))



    


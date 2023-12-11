# #   https://leetcode.com/problems/island-perimeter/
# 463. Island Perimeter
# Easy
# 6.1K
# 312
# Companies
# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

# Example 1:


# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# Example 2:

# Input: grid = [[1]]
# Output: 4
# Example 3:

# Input: grid = [[1,0]]
# Output: 4

from typing import List
def islandPerimeter( grid: List[List[int]]) -> int:
    R = len(grid)
    C = len(grid[0])
    perimeter = 0 
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1:
                perimeter +=4
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -=2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -=2
    return perimeter



if __name__ == "__main__":
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print ("{}".format(islandPerimeter(grid)))
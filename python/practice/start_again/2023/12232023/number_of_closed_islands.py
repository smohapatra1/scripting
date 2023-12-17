# #   https://leetcode.com/problems/number-of-closed-islands/

# 1254. Number of Closed Islands
# Medium
# 4.4K
# 154
# Companies
# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

# Return the number of closed islands.

 

# Example 1:



# Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation: 
# Islands in gray are closed because they are completely surrounded by water (group of 1s).
# Example 2:



# Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# Output: 1
# Example 3:

# Input: grid = [[1,1,1,1,1,1,1],
#                [1,0,0,0,0,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,1,0,1,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,0,0,0,0,1],
#                [1,1,1,1,1,1,1]]
# Output: 2

def NumClosedIsland( grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    count = 0 
    def dfs(i, j):
        if i < 0 or j < 0 or i >= rows or j >=cols:
            return False
        if grid[i][j] == 1:
            return True
        grid[i][j] = 1
        left = dfs(i, j - 1)
        right = dfs(i, j+1)
        up = dfs(i-1, j )
        down = dfs(i+1, j )
        return left and right and up and down 
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0 and dfs(i, j ):
                count +=1
    return count



if __name__ == "__main__":
    grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
    print ("{}".format(NumClosedIsland(grid)))
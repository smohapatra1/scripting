# #   https://leetcode.com/problems/shortest-bridge/

# 934. Shortest Bridge
# Medium
# 5.2K
# 194
# Companies
# You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

# An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

# You may change 0's to 1's to connect the two islands to form one island.

# Return the smallest number of 0's you must flip to connect the two islands.

 

# Example 1:

# Input: grid = [[0,1],[1,0]]
# Output: 1
# Example 2:

# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
# Example 3:

# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1

from typing import List
def shortestBridge(grid: List[List[int]]) -> int:
    m=len(grid)
    n=len(grid[0])
    i, j = next((i,j) for i in range(m) for j in range(n) if grid[i][j])
    stack = [(i,j)]
    seen = set(stack)
    while stack:
        i, j = stack.pop()
        seen.add((i,j))
        for ii, jj in (i-1, j ), (i, j-1), (i, j+1), (i+1,j ):
            if 0 <= ii <  m and 0 <=jj  < n and grid[ii][jj] and (ii, jj) not in seen:
                stack.append((ii, jj))
                seen.add((ii, jj))
    ans = 0 
    queue = list(seen)
    while queue:
        newq = []
        for i, j in queue:
            for ii, jj in (i-1, j ), (i, j-1), (i, j+1), (i+1, j ):
                if  0 <= ii < m and 0 <=jj < n and (ii, jj) not in seen:
                    if grid[ii][jj] == 1: return ans
                    newq.append((ii, jj))
                    seen.add((ii, jj))
            queue = newq
            ans +=1




if __name__ == "__main__":
    grid = [[0,1],[1,0]]
    print ("{}".format(shortestBridge(grid)))
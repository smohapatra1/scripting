#   https://neetcode.io/practice
# 994. Rotting Oranges
# Medium
# 11.7K
# 366
# Companies
# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

# Example 1:


# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

from typing import List
from collections import deque
def orangesRotting(grid: List[List[int]]) -> int:
    r=len(grid)
    c=len(grid[0])
    fresh=set()
    rotten=deque()
    for row in range(r):
        for col in range(c):
            if grid[row][col] == 1:
                fresh.add((row, col))
            elif grid [row][col] == 2:
                rotten.append((row,col))
    minutes=0
    while fresh and rotten:
        minutes +=1
        for rot in range(len(rotten)):
            row, col = rotten.popleft()
            for direction in ((row-1, col), (row+1, col), (row, col+1), (row, col-1)):
                if direction in fresh:
                    fresh.remove(direction) # Remove and add into rotton 
                    rotten.append(direction) # 
    return -1 if fresh else minutes

if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    #grid = [[2,1,1],[0,1,1],[1,0,1]]
    print ("{}".format(orangesRotting(grid)))

    
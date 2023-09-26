# #   https://leetcode.com/problems/surrounded-regions/
# 130. Surrounded Regions
# Medium
# 7.9K
# 1.6K
# Companies
# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

# Example 1:


# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.
# Example 2:

# Input: board = [["X"]]
# Output: [["X"]]


from typing import List

def solve(board: List[List[str]]) -> None:
    if not board:
        return 
    m=len(board)
    n=len(board[0])
    def dfs(i:int, j:int ) -> None:
        if i<0 or i >=m or j < 0 or j >=n or board[i][j] !='O':
            return 
        board[i][j] = '#' # Mark as visited 
        #Mark all adjacent 0's
        dfs(i+1, j )
        dfs(i-1, j )
        dfs(i, j+1)
        dfs(i, j-1)
    for i in range(m):
        dfs(i, 0 )
        dfs(i, n-1)
    for j in range(n):
        dfs(0, j )
        dfs(m-1, j )
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == '#':
                board[i][j] ='O'
if __name__ == "__main__":
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    print ("{}".format(solve(board)))

        




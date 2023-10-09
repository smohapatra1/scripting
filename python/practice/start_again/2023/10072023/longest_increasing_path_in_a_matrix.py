# #   https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

# 329. Longest Increasing Path in a Matrix
# Hard
# 8.6K
# 127
# Companies
# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

# Example 1:


# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# Example 2:


# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
# Example 3:

# Input: matrix = [[1]]
# Output: 1

from typing import List
from functools import lru_cache
def longest_Matrix(matrix : List[List[int]]) -> int:
    m=len(matrix)
    n=len(matrix[0])
    directions=[0,1,0,-1,0]
    @lru_cache(maxsize=None)
    def dfs(r,c):
        ans=1
        for i in range(4):
            new_row=r+directions[i]
            new_col=c+directions[i+1]
            if 0<=new_row<m and 0<=new_col<n and matrix[new_row][new_col]>matrix[r][c]:
                ans=max(ans, dfs(new_row, new_col)+1)
        return ans
    return max(dfs(r,c) for r in range(m) for c in range(n))



if __name__ == "__main__":
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    #matrix = [[3,4,5],[3,2,6],[2,2,1]]
    print ("{}".format(longest_Matrix(matrix)))

#   https://leetcode.com/problems/set-matrix-zeroes/

# 73. Set Matrix Zeroes
# Medium
# 13.3K
# 658
# Companies
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

 

# Example 1:


# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2:


# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


from typing import List
def setZeros( matrix: List[List[int]]) -> None:
    if not matrix:
        return []
    m=len(matrix)
    n=len(matrix[0])
    zeros_row= [False] * m 
    zeros_col= [False] * n 
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                zeros_row[row] = True
                zeros_col[col] = True
    for row in range(m):
        for col in range(n):
            if zeros_row[row] or zeros_col[col]:
                matrix[row][col] = 0 

if __name__ == "__main__":
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print ("{}".format(setZeros(matrix)))


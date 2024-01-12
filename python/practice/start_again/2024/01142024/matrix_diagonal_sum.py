# #   https://leetcode.com/problems/matrix-diagonal-sum/

# 1572. Matrix Diagonal Sum
# Easy

# Topics
# Companies

# Hint
# Given a square matrix mat, return the sum of the matrix diagonals.

# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

# Example 1:


# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.
# Example 2:

# Input: mat = [[1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1]]
# Output: 8
# Example 3:

# Input: mat = [[5]]
# Output: 5
 
from typing import List
def MatrixDiagonal( mat: List[List[int]]) -> int :
    n=len(mat)
    s=0
    for i in range(n):
        s+=mat[i][i]
        mat[i][i] = 0 
        s+=mat[-i-1][i]
    return s

if __name__ == "__main__":
    mat = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    print ("{}".format(MatrixDiagonal(mat)))
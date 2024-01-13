# #   https://leetcode.com/problems/spiral-matrix/description/

# 54. Spiral Matrix
# Solved
# Medium

# Topics
# Companies

# Hint
# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

from typing import List
def SpiralMatrix(matrix: List[List[int]]) -> List[int]:
    res =[]
    while matrix:
        res.extend(matrix.pop(0))
        matrix=[*zip(*matrix)][::-1]
    return res


if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print ("{}".format(SpiralMatrix(matrix)))
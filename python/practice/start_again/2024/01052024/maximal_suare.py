# #   https://leetcode.com/problems/maximal-square/

# 221. Maximal Square
# Medium
# 9.8K
# 211
# Companies
# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

# Example 1:


# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
# Example 2:


# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
# Example 3:

# Input: matrix = [["0"]]
# Output: 0
from typing import List
def MaxSquare(matrix : List[List[int]]) -> int:
    m=len(matrix)
    n=len(matrix[0])
    result=0
    prev = [0] * n
    curr = [0] * n 
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                curr[j] = min(curr[j-1] if j > 0 else 0,
                              prev[j-1] if j > 0 else 0,
                              prev[j])+ 1
                if curr[j] > result:
                    result=curr[j]
        prev=curr
        curr=[0]*n
    return result*result


if __name__ == "__main__":
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print ("{}".format(MaxSquare(matrix)))

# #   https://leetcode.com/problems/spiral-matrix-ii/description/

# 59. Spiral Matrix II
# Medium

# Topics
# Companies
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

# Example 1:


# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# Example 2:

# Input: n = 1
# Output: [[1]]

from typing import List
def SpiralMatrix(n: int ) -> List[List[int]]:
    res=[[n*n]]
    positive = n*n
    while positive > 1:
        positive, hi = positive - len(res), positive
        res = [[ i for i in range(positive, hi)]] + [list(j) for j in zip(*res[::-1])]

    return res

if __name__ == "__main__":
    n=3
    print ("{}".format(SpiralMatrix(n)))
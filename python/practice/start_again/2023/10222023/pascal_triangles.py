# # https://leetcode.com/problems/pascals-triangle/
# 118. Pascal's Triangle
# Easy
# 12K
# 379
# Companies
# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]


def Pascal_Triangle(numRows : int ):
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    prevRow=generate(numRows -1)
    newRow = [1] * numRows
    for i in range(1, numRows -1):
        numRows[i] = prevRow[-1][i-1] + prevRow[-1][i]
    prevRow.append(newRow)
    return prevRow


if __name__ == "__main__":
    numRows = 5
    print ("{}".format(Pascal_Triangle(numRows)))
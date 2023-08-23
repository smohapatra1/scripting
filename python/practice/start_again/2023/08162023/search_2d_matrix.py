# 74. Search a 2D Matrix
# Medium

# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

def SearchMatrix(matrix, target):
    #Solution-01
    #where m is the number of rows and n is the number of columns in matrix
    #return any(target in row for row in matrix)
    # Solution-02
    for row in matrix:
        if row[-1] >=target:
            return target in row
        return False


if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target=3
    # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    # target = 13
    print ("{} in {}".format(SearchMatrix(matrix, target), matrix))

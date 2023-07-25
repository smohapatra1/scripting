# 36. Valid Sudoku

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

# Algorithm
# Check if the rows and columns contain values 1-9, without repetition.
# If any row or column violates this condition, the Sudoku board is invalid.
# Check to see if each of the 9 sub-squares contains values 1-9, without repetition. If they do, the Sudoku board is valid; otherwise, it is invalid.


# Checks whether there is any duplicate in current row or not

def NotInRow(arr, row):
    st=set()
    for i in range(0,9):
        # If already encountered before,
        # return false
        if arr[row][i] in st:
            return False
        # If it is not an empty cell, insert value
        # at the current cell in the set
        if arr[row][i] != '.':
            st.add(arr[row][i])
    return True

# Checks whether there is any duplicate in current column or not

def NotInCol(arr, col):
    st=set()
    for i in range(0,9):
        if arr[i][col] in st:
            return False
        if arr[i][col] !='.':
            st.add(arr[i][col])
    return True

# Checks whether there is any duplicate in current 3x3 box or not.

def NotInBox(arr, StartRow, StartCol):
    st=set()
    for row in range(0,3):
        for col in range(0,3):
            curr=arr[row + StartRow][col + StartCol]
            if curr in st:
                return False 
            if curr != '.':
                st.add(curr)
    return True 
# Checks whether current row and current column and current 3x3 box is valid or not
def isValid(arr,row, col):
    return (NotInRow(arr,row) and NotInCol(arr,row) and NotInBox(arr, row-row %3 , col - col %3 ))
def IsValidConfig(arr,n):
    for i in range(0,n):
        for j in range(0,n):
            if not isValid(arr, i, j ):
                return False
    return True


if __name__ == "__main__":
    #Valid 
    # board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    #          ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    #          ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    #          ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    #          ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    #          ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    #          ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    #          ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    #          ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
    #InValid 
    board = [['8', '3', '.', '.', '7', '.', '.', '.', '.'],
             ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
             ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
             ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
             ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
             ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
             ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
             ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
             ['.', '.', '.', '.', '8', '.', '.', '7', '9']]

    if IsValidConfig(board, 9 ):
        print ("YES")
    else:
        print ("NO")



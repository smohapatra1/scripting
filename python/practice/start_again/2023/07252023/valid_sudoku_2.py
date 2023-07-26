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

from typing import List
def isValidSudoku(self, board : List[List[str]]) -> bool:
    
    ## Method - 01 
    # res = []
    # for i in range(9):
    #     for j in range(9):
    #         element = board[i][j]
    #         if element != '.':
    #             res += [(i, element), (element, j), (i // 3, j // 3, element)]
    # return len(res) == len(set(res))
    
    ## Method - 02  

    res=[]
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if x !='.':
                res +=[(i, x), ( x,j), (i//3, j//3, x)]
    return len(res) == len(set(res))

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
    if isValidSudoku(board, 9 ):
        print ("YES")
    else:
        print ("NO")
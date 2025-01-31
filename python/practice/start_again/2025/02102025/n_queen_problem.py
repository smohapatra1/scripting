#   https://www.geeksforgeeks.org/python-program-for-n-queen-problem-backtracking-3/

global N
N = 4 

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print (board[i][j], end = " ")
        print()


def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solvenqUtil(board, col):
    if col >= N :
        return True
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solvenqUtil(board, col +1) == True:
                return True
            board[i][col] = 0
    return False

def solveNq():
    board = [ [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]
             ]
    if solvenqUtil(board, 0) == False:
        print ("Solution doesn't exist ")
        return False
    printSolution(board)
    return True

solveNq()
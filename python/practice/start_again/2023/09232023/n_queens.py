# 51. N-Queens
# Hard
# 11.4K
# 239
# Companies
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

# Example 1:


# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:

# Input: n = 1
# Output: [["Q"]]


from typing import List
def Nqueens(n: str) -> List[List[str]]:
    state=[["."] * n for _ in range(n)]
    result=[]
    visited_cols=set()
    visited_diagonals=set()
    visited_antidiagonals=set()
    def backtrack(r):
        if r == n:
            result.append(["".join(row) for row in state])
            return 
        for c in range(n):
            diff = r - c
            _sum=r+c 
            if not (c in visited_cols or diff in visited_diagonals or _sum in visited_diagonals):
                visited_cols.add(c)
                visited_diagonals.add(diff)
                visited_antidiagonals.add(_sum)
                state[r][c] = 'Q'
                backtrack(r+1)
                visited_cols.remove(c)
                visited_diagonals.remove(diff)
                visited_antidiagonals.remove(_sum)
                state[r][c]='.'
    backtrack(0)
    return result
if __name__ == "__main__":
    n=4
    print ("{}".format(Nqueens(n)))


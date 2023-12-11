# # https://leetcode.com/problems/n-queens-ii/
# 52. N-Queens II
# Hard
# 3.7K
# 254
# Companies
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

# Example 1:


# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
# Example 2:

# Input: n = 1
# Output: 1

def Queens_II( n: int ) -> int:
    res =0 
    col = set()
    pos = set()
    neg = set()
    def backtracking(r):
        if n ==r :
            nonlocal res
            res +=1
        for c in range(n):
            if c in col or (c+r) in pos or (r-c) in neg:
                continue
            col.add(c)
            pos.add(c+r)
            neg.add(r-c)
            backtracking(r+1)
            col.remove(c)
            pos.remove(c+r)
            neg.remove(r-c)
    backtracking(0)
    return res




if __name__ == "__main__":
    n=4 
    print ("{}".format(Queens_II(n)))
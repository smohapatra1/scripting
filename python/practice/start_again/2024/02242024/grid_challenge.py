# #   https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four

# Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.

# Example

# The grid is illustrated below.

# a b c
# a d e
# e f g
# The rows are already in alphabetical order. The columns a a e, b d f and c e g are also in alphabetical order, so the answer would be YES. Only elements within the same row can be rearranged. They cannot be moved to a different row.

# Function Description

# Complete the gridChallenge function in the editor below.

# gridChallenge has the following parameter(s):

# string grid[n]: an array of strings
# Returns

# string: either YES or NO
# Input Format

# The first line contains , the number of testcases.

# Each of the next  sets of lines are described as follows:
# - The first line contains , the number of rows and columns in the grid.
# - The next  lines contains a string of length 

# Constraints



# Each string consists of lowercase letters in the range ascii[a-z]

# Output Format

# For each test case, on a separate line print YES if it is possible to rearrange the grid alphabetically ascending in both its rows and columns, or NO otherwise.

# Sample Input

# STDIN   Function
# -----   --------
# 1       t = 1
# 5       n = 5
# ebacd   grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
# fghij
# olmkn
# trpqs
# xywuv
# Sample Output

# YES
# Explanation

# The x grid in the  test case can be reordered to

# abcde
# fghij
# klmno
# pqrst
# uvwxy
# This fulfills the condition since the rows 1, 2, ..., 5 and the columns 1, 2, ..., 5 are all alphabetically sorted.

def gridChallenge(grid):
    n=len(grid)
    rows=[[0] for i in range(n)]
    for i, item in enumerate(grid):
        rows[i] = [*item]
    m=len(rows[0])
    for j in range(m):
        column=''.join(rows[i][j] for i in range(n))
        if column !=''.join(sorted(column)):
            return 'NO'
    return 'YES' 


if __name__ == "__main__":
    t=int(input().strip())
    for t_iter in range(n):
        arr=int(input().strip())
        grid=[]
        for _ in range(arr):
            grid_item=input()
            grid.append(grid_item)
        result=gridChallenge(grid)
        print (result)
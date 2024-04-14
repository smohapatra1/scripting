# #   https://www.hackerrank.com/challenges/xor-matrix/problem?isFullScreen=true

# Consider a zero-indexed matrix with  rows and  columns, where each row is filled gradually. Given the first row of the matrix, you can generate the elements in the subsequent rows using the following formula:

# Each row is generated one by one, from the second row through the last row. Given the first row of the matrix, find and print the elements of the last row as a single line of space-separated integers.

# Note: The  operator denotes bitwise XOR.

# Input Format

# The first line contains two space-separated integers denoting the respective values of  (the number of columns in the matrix) and  (the number of rows in the matrix).
# The second line contains  space-separated integers denoting the respective values of the elements in the matrix's first row.

# Constraints

# Output Format

# Print  space-separated integers denoting the respective values of the elements in the last row of the matrix.

# Sample Input 0

# 4 2
# 6 7 1 3
# Sample Output 0

# 1 6 2 5
# Explanation 0

# We use the formula given above to calculate the  values in the last row of the matrix:

# We then print each value (in order) as a single line of space-separated integers.



#!/bin/python3

import os
import sys

#
# Complete the xorMatrix function below.
#
def xorMatrix(m, first_row):
    #
    # Write your code here.
    #
    n = len(first_row)
    m -=1
    mb = str(bin(m))[2:]
    lmb = len(mb)
    result = first_row.copy()
    for i in range(lmb):
        if mb[i] == '1':
            tmp = result.copy()
            offset = 2 ** (lmb - 1 - i )
            for j in range(n):
                result [j] = tmp[j] ^ tmp[(j+offset)%n]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    first_row = list(map(int, input().rstrip().split()))

    last_row = xorMatrix(m, first_row)

    fptr.write(' '.join(map(str, last_row)))
    fptr.write('\n')

    fptr.close()

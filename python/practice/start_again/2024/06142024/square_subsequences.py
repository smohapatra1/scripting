#   https://www.hackerrank.com/challenges/square-subsequences/problem?isFullScreen=true


# Square Subsequences

# A string is called a square string if it can be obtained by concatenating two copies of the same string. For example, "abab", "aa" are square strings, while "aaa", "abba" are not. Given a string, how many (non-empty) subsequences of the string are square strings? A subsequence of a string can be obtained by deleting zero or more characters from it, and maintaining the relative order of the remaining characters.

# Input Format

# The first line contains the number of test cases, .
#  test cases follow. Each case contains a string, .

# Output Format

# Output  lines, one for each test case, containing the required answer modulo 1000000007.

# Constraints:

#  will have at most  lowercase characters ('a' - 'z').

# Sample Input

# 3
# aaa
# abab
# baaba

# Sample Output

# 3
# 3
# 6

# Explanation

# For the first case, there are 3 subsequences of length 2, all of which are square strings.
# For the second case, the subsequences "abab", "aa", "bb" are square strings.
# Similarly, for the third case, "bb", "baba" (twice), and "aa" (3 of them) are the square subsequences.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squareSubsequences' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

NUMBER = 1000000007

def solve_sub(string, size):
    s1 = string[:size]
    size1 = len(s1) + 1
    s2 = string[size:]
    size2 = len(s2) + 1
    N = [[0 for j in range(size2)] for i in range(size1)]

    for i in range(1, size1):
        for j in range(1, size2):
            if s1[i - 1] == s2[j - 1]:
                N[i][j] = N[i - 1][j] + N[i][j - 1] + 1
            else:
                N[i][j] = N[i - 1][j] + N[i][j - 1] - N[i - 1][j - 1]

    return N[-1][-1] - N[-2][-1]

def solve(string):
    count = sum(solve_sub(string, i) for i in range(1, len(string)))
    return count % NUMBER

if __name__ == '__main__':
    import sys
    _ = sys.stdin.readline()
    for line in sys.stdin:
        print(solve(line.strip()))
        

# def squareSubsequences(s):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         s = input()

#         result = squareSubsequences(s)

#         fptr.write(str(result) + '\n')

#     fptr.close()

# #   https://www.hackerrank.com/challenges/dynamic-programming-classics-the-longest-common-subsequence/problem?isFullScreen=true

# A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. Longest common subsequence (LCS) of 2 sequences is a subsequence, with maximal length, which is common to both the sequences.

# Given two sequences of integers,  and , find the longest common subsequence and print it as a line of space-separated integers. If there are multiple common subsequences with the same maximum length, print any one of them.

# In case multiple solutions exist, print any of them. It is guaranteed that at least one non-empty common subsequence will exist.

# Recommended References

# This Youtube video tutorial explains the problem and its solution quite well.


# Function Description

# Complete the longestCommonSubsequence function in the editor below. It should return an integer array of a longest common subsequence.

# longestCommonSubsequence has the following parameter(s):

# a: an array of integers
# b: an array of integers
# Input Format

# The first line contains two space separated integers  and , the sizes of sequences  and .
# The next line contains  space-separated integers .
# The next line contains  space-separated integers .

# Constraints





# Constraints



# Output Format

# Print the longest common subsequence as a series of space-separated integers on one line. In case of multiple valid answers, print any one of them.

# Sample Input

# 5 6
# 1 2 3 4 1
# 3 4 1 2 1 3
# Sample Output

# 1 2 3
# Explanation

# There is no common subsequence with length larger than 3. And "1 2 3", "1 2 1", "3 4 1" are all correct answers.

# Tested by Khongor


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'longestCommonSubsequence' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

n,m = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

s_lengths = [[0 for _ in range(m+1)] for _ in range(n+1)]
sequences = [[[] for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if A[i-1] == B[j-1]:
            s_lengths[i][j] = 1 + s_lengths[i-1][j-1]
            sequences[i][j] = list(sequences[i-1][j-1])
            sequences[i][j].append(A[i-1])
        else:
            if s_lengths[i-1][j] >= s_lengths[i][j-1]:
                s_lengths[i][j] = s_lengths[i-1][j]
                sequences[i][j] = sequences[i-1][j]
            else:
                s_lengths[i][j] = s_lengths[i][j-1]
                sequences[i][j] = sequences[i][j-1]
            
print(" ".join(map(str,sequences[-1][-1])))

# def longestCommonSubsequence(a, b):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     m = int(first_multiple_input[1])

#     a = list(map(int, input().rstrip().split()))

#     b = list(map(int, input().rstrip().split()))

#     result = longestCommonSubsequence(a, b)

#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()

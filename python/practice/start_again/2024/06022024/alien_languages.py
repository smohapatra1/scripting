# #   https://www.hackerrank.com/challenges/alien-languages/problem?isFullScreen=true

# Sophia has discovered several alien languages. Suprisingly, all of these languages have an alphabet, and each of them may contain thousands of characters! Also, all the words in a language have the same number of characters in it.

# However, the aliens like their words to be aesthetically pleasing, which for them means that for the  letter of an -letter alphabet (letters are indexed ):

# if , then the  letter may be the last letter of a word, or it may be immediately followed by any letter, including itself.

# if , then the  letter can not be the last letter of a word and also can only be immediately followed by  letter if and only if .

# Sophia wants to know how many different words exist in this language. Since the result may be large, she wants to know this number, modulo .

# Input Format

# The first line contains , the number of test cases. The first line is followed by  lines, each line denoting a test case. Each test case will have two space-separated integers ,  which denote the number of letters in the language and the length of words in this language respectively.

# Constraints

# Output Format

# For each test case, output the number of possible words modulo .

# Sample Input

# 3
# 1 3
# 2 3
# 3 2
# Sample Output

# 1
# 3
# 6
# Explanation

# For the first test case, there's one letter ('a') and all the words consist of  letters. There's only one possibility which is "aaa".

# For the second test case, there are two letters ('a' and 'b') and all the words are of  letters. The possible strings are "abb", "bab", & "bbb". The words can end only with 'b' because  and for 'a', it's . "aab" is not allowed because 'a' can not be followed immediately by 'a'. For a word of length 4 and alphabet of size 2, "abab" would be allowed.

# For the third test case, there are three letters ('a', 'b' and 'c') and all of the words are  letters. The words can only end with 'b' or 'c'. The possible words are "ab", "ac", "bb", "cc", "bc", "cb".



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alienLanguages' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

mod = 10**8 + 7

for cas in range(int(input())):
    n, m = map(int, input().strip().split())
    v = [2*i > n for i in range(n+1)]
    for i in range(n-1,-1,-1):
        v[i] += v[i + 1]
    c = []
    while v[1]:
        c.append(v[1])
        for i in range(1,n//2+1):
            v[i] = v[2*i]
        for i in range(n//2+1,n+1):
            v[i] = 0
        for i in range(n-1,-1,-1):
            v[i] = (v[i] + v[i + 1]) % mod

    f = [1] + [0]*(len(c)-1)
    for k in range(1,m+1):
        f = [sum(F * C for F, C in zip(f, c)) % mod] + f[:-1]

    print(f[0])

# def alienLanguages(n, m):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         first_multiple_input = input().rstrip().split()

#         n = int(first_multiple_input[0])

#         m = int(first_multiple_input[1])

#         result = alienLanguages(n, m)

#         fptr.write(str(result) + '\n')

#     fptr.close()

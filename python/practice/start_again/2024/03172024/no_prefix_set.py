# #   https://www.hackerrank.com/challenges/one-month-preparation-kit-no-prefix-set/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-four
# There is a given list of strings where each string contains only lowercase letters from , inclusive. The set of strings is said to be a GOOD SET if no string is a prefix of another string. In this case, print GOOD SET. Otherwise, print BAD SET on the first line followed by the string being checked.

# Note If two strings are identical, they are prefixes of each other.

# Example

# Here 'abcd' is a prefix of 'abcde' and 'bcd' is a prefix of 'bcde'. Since 'abcde' is tested first, print

# BAD SET  
# abcde
# .

# No string is a prefix of another so print

# GOOD SET 
# Function Description
# Complete the noPrefix function in the editor below.

# noPrefix has the following parameter(s):
# - string words[n]: an array of strings

# Prints
# - string(s): either GOOD SET or BAD SET on one line followed by the word on the next line. No return value is expected.

# Input Format
# First line contains , the size of .
# Then next  lines each contain a string, .

# Constraints

#  the length of words[i] 
# All letters in  are in the range 'a' through 'j', inclusive.

# Sample Input00

# STDIN       Function
# -----       --------
# 7            words[] size n = 7
# aab          words = ['aab', 'defgab', 'abcde', 'aabcde', 'bbbbbbbbbb', 'jabjjjad']
# defgab  
# abcde
# aabcde
# cedaaa
# bbbbbbbbbb
# jabjjjad
# Sample Output00

# BAD SET
# aabcde
# Explanation
# 'aab' is prefix of 'aabcde' so it is a BAD SET and fails at string 'aabcde'.

# Sample Input01

# 4
# aab
# aac
# aacghgh
# aabghgh
# Sample Output01

# BAD SET
# aacghgh
# Explanation
# 'aab' is a prefix of 'aabghgh', and aac' is prefix of 'aacghgh'. The set is a BAD SET. 'aacghgh' is tested before 'aabghgh', so and it fails at 'aacghgh'.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    # Write your code here
    N=len(words)
    first = 2*N
    s=list(enumerate(words))
    s.sort(key = lambda x: x[1])
    for i in range(N-1):
        for j in range(i+1 , N):
            a, b = s[i][1], s[j][1]
            if len(a) > len(b): continue
            if a != b[:len(a)]: break
            first = min(first, max(s[i][0], s[j][0]))
    if first == 2*N:
        print ("GOOD SET")
    else:
        print ("BAD SET")
        print (words[first])

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)

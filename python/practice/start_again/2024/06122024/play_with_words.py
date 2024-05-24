# #   https://www.hackerrank.com/challenges/strplay/problem?isFullScreen=true

# Shaka and his brother have created a boring game which is played like this:

# They take a word composed of lowercase English letters and try to get the maximum possible score by building exactly 2 palindromic subsequences. The score obtained is the product of the length of these 2 subsequences.

# Let's say  and  are two subsequences from the initial string. If  &  are the smallest and the largest positions (from the initial word) respectively in  ; and  &  are the smallest and the largest positions (from the initial word) respectively in , then the following statements hold true:
# ,
# , &
# .
# i.e., the positions of the subsequences should not cross over each other.

# Hence the score obtained is the product of lengths of subsequences  & . Such subsequences can be numerous for a larger initial word, and hence it becomes harder to find out the maximum possible score. Can you help Shaka and his brother find this out?

# Input Format

# Input contains a word  composed of lowercase English letters in a single line.

# Constraints


# each character will be a lower case english alphabet.

# Output Format

# Output the maximum score the boys can get from .

# Sample Input

# eeegeeksforskeeggeeks
# Sample Output

# 50
# Explanation

# A possible optimal solution is eee-g-ee-ksfor-skeeggeeks being eeeee the one subsequence and skeeggeeks the other one. We can also select eegee in place of eeeee, as both have the same length.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'playWithWords' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def playWithWords(s):
    # Write your code here
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    # Every individual char is a palindrome of 1
    for i in range(n):
        dp[i][i] = 1
        
    # Get longest palindromic subsequences
    for start in range(n - 1, -1, -1):
        for end in range(start + 1, n):
            if s[start] == s[end]:
                dp[start][end] = 2 + dp[start + 1][end - 1]
            else:
                dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])
    
    # Get max product from DP table by calculating non-overlapping
    max_prod = 0
    for sub1_end in range(n - 1):
        sub2_start = sub1_end + 1
        max_prod = max(max_prod, dp[0][sub1_end] * dp[sub2_start][n - 1])
    return max_prod

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = playWithWords(s)

    fptr.write(str(result) + '\n')

    fptr.close()

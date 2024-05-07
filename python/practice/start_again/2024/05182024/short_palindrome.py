# #   https://www.hackerrank.com/challenges/short-palindrome/problem?isFullScreen=true

# Consider a string, , of  lowercase English letters where each character,  (, denotes the letter at index  in . We define an  palindromic tuple of  to be a sequence of indices in  satisfying the following criteria:

# , meaning the characters located at indices  and  are the same.
# , meaning the characters located at indices  and  are the same.
# , meaning that , , , and  are ascending in value and are valid indices within string .
# Given , find and print the number of  tuples satisfying the above conditions. As this value can be quite large, print it modulo .

# Function Description
# Complete the function shortPalindrome in the editor below.

# shortPalindrome has the following paramter(s):
# - string s: a string

# Returns
# - int: the number of tuples, modulo 

# Input Format

# A single string, .

# Constraints

# It is guaranteed that  only contains lowercase English letters.
# Sample Input 0

# kkkkkkz
# Sample Output 0

# 15
# Explanation 0

# The letter z will not be part of a valid tuple because you need at least two of the same character to satisfy the conditions defined above. Because all tuples consisting of four k's are valid, we just need to find the number of ways that we can choose four of the six k's. This means our answer is .

# Sample Input 1

# ghhggh
# Sample Output 1

# 4
# Explanation 1

# The valid tuples are:

# Thus, our answer is .

# Sample Input 0

# kkkkkkz
# Sample Output 0

# 15
# Sample Input 1

# abbaab
# Sample Output 1

# 4
# Sample Input 2

# akakak
# Sample Output 2

# 2
# Explanation 2

# Tuples possible are 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'shortPalindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def shortPalindrome(s):
    # Write your code here
    charCount = {}
    pairCount = {}
    pairHash = {}
    totalCount = 0
    MOD = 10**9 + 7

    for char in s:
        charIndex = ord(char) - ord('a')
        pairIndex = charIndex
        totalCount = (totalCount + pairCount.get(charIndex, 0)) % MOD

        for pairChar in range(26):
            pairCount[pairChar] = (pairCount.get(pairChar, 0) + pairHash.get(pairIndex, 0)) % MOD
            pairHash[pairIndex] = (pairHash.get(pairIndex, 0) + charCount.get(pairChar, 0)) % MOD
            pairIndex += 26

        charCount[charIndex] = charCount.get(charIndex, 0) + 1

    return totalCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = shortPalindrome(s)

    fptr.write(str(result) + '\n')

    fptr.close()

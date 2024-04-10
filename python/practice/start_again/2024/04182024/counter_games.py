# #   https://www.hackerrank.com/challenges/counter-game/problem?isFullScreen=true

# Louise and Richard have developed a numbers game. They pick a number and check to see if it is a power of . If it is, they divide it by . If not, they reduce it by the next lower number which is a power of . Whoever reduces the number to  wins the game. Louise always starts.

# Given an initial value, determine who wins the game.

# Example

# It's Louise's turn first. She determines that  is not a power of . The next lower power of  is , so she subtracts that from  and passes  to Richard.  is a power of , so Richard divides it by  and passes  to Louise. Likewise,  is a power so she divides it by  and reaches . She wins the game.

# Update If they initially set counter to , Richard wins. Louise cannot make a move so she loses.

# Function Description

# Complete the counterGame function in the editor below.

# counterGame has the following parameter(s):

# int n: the initial game counter value
# Returns

# string: either Richard or Louise
# Input Format

# The first line contains an integer , the number of testcases.
# Each of the next  lines contains an integer , the initial value for each game.

# Constraints

# Sample Input 0

# 1
# 6
# Sample Output 0

# Richard
# Explanation 0

#  is not a power of  so Louise reduces it by the largest power of  less than :.
#  is a power of  so Richard divides by  to get  and wins the game.



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    # Write your code here
    res = 1 
    x = bin(n)[2:]
    y = x.rstrip('0')
    a = len(x) - len(y)
    for k in y :
        res ^= int(k)
    b = res^(a%2)
    return 'Louise' if b == 1  else 'Richard'
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()

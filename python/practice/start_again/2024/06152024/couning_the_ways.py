# #   https://www.hackerrank.com/challenges/count-ways-1/problem?isFullScreen=true

# Little Walter likes playing with his toy scales. He has  types of weights. The  weight type has weight . There are infinitely many weights of each type.

# Recently, Walter defined a function, , denoting the number of different ways to combine several weights so their total weight is equal to . Ways are considered to be different if there is a type which has a different number of weights used in these two ways.

# For example, if there are  types of weights with corresonding weights , , and , then there are  ways to get a total weight of :

# Use  weights of type .
# Use  weights of type .
# Use  weight of type  and  weight of type .
# Use  weight of type .
# Given , , , and , can you find the value of ?

# Input Format

# The first line contains a single integer, , denoting the number of types of weights.
# The second line contains  space-separated integers describing the values of , respectively
# The third line contains two space-separated integers denoting the respective values of  and .

# Constraints

# Note: The time limit for C/C++ is  second, and for Java it's  seconds.

# Output Format

# Print a single integer denoting the answer to the question. As this value can be very large, your answer must be modulo .

# Sample Input

# 3
# 1 2 3
# 1 6
# Sample Output

# 22
# Explanation



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countWays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. LONG_INTEGER l
#  3. LONG_INTEGER r
#

MOD = 10**9 + 7

def lcm(lst):
    ans = 1
    for x in lst:
        ans = ans*x//gcd(ans, x)
    return ans

def gcd(a,b):
    if a<b:
        a, b = b, a
    while b > 0:
        a, b = b, a%b
    return a

def getsoltable(a, m, MOD=MOD):
    soltable = [1] + [0] * (len(a)*m-1)
    for x in a:
        oldsoltable = soltable
        soltable = list(soltable)
        for i in range(x, len(soltable)):
            soltable[i] = (oldsoltable[i] + soltable[i - x]) % MOD
    return soltable

def countsols(const, soltable, lcm):
    offset = const % lcm
    pts = soltable[offset::lcm]
    assert len(pts) == len(a)
    coef = polycoef(pts)
    return polyval(coef, const//lcm)

def polycoef(pts):
    coef = []
    for x, y in enumerate(pts):
        fact = descpower = 1
        for i, c in enumerate(coef):
            y -= descpower*c//fact
            descpower *= x - i
            fact *= i + 1
        coef.append(y)
    return coef
        
def polyval(coef, x):
    ans = 0
    fact = descpower = 1
    for i, c in enumerate(coef):
        ans += c * descpower * pow(fact, MOD-2, MOD)
        descpower = descpower * (x - i) % MOD
        fact *= i + 1
    return ans % MOD
        
n = int(input())
a = [1] + [int(fld) for fld in input().strip().split()]
L, R = [int(fld ) for fld in input().strip().split()]
m = lcm(a)
soltable = getsoltable(a, m)
print((countsols(R, soltable, m) - countsols(L-1, soltable, m)) % MOD)


# def countWays(arr, l, r):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     arr_count = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     first_multiple_input = input().rstrip().split()

#     l = int(first_multiple_input[0])

#     r = int(first_multiple_input[1])

#     result = countWays(arr, l, r)

#     fptr.write(str(result) + '\n')

#     fptr.close()





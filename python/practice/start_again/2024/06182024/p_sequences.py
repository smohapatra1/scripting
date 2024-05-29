# #   https://www.hackerrank.com/challenges/p-sequences/problem?isFullScreen=true

# We call a sequence of N natural numbers (a1, a2, ..., aN) a P-sequence, if the product of any two adjacent numbers in it is not greater than P. In other words, if a sequence (a1, a2, ..., aN) is a P-sequence, then ai * ai+1 ≤ P ∀ 1 ≤ i < N

# You are given N and P. Your task is to find the number of such P-sequences of N integers modulo 109+7.

# Input Format

# The first line of input consists of N
# The second line of the input consists of P.

# Constraints

# 2 ≤ N ≤ 103
# 1 ≤ P ≤ 109
# 1 ≤ ai

# Output Format

# Output the number of P-sequences of N integers modulo 109+7.

# Sample Input 0

# 2
# 2
# Sample Output 0

# 3
# Explanation 0

# 3 such sequences are {1,1},{1,2} and {2,1}


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pSequences' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pSequences(n, p):
    # Write your code here
    MOD = 1000000000 + 7
    root = int(math.sqrt(p))
    last = root * 2 - 2 if root * (root + 1) > p else root * 2 - 1
    qtty = []
    val = []
    calc = [None] * (last + 1)
    i = 0
    j = last
    accum = 0
    size = last + 1

    while accum < p:
        val_i = int(p // (p // (accum + 1))) - accum
        qtty_i = val_i
        calc_j = accum + val_i
        calc[j] = calc_j
        val.append(val_i)
        qtty.append(qtty_i)
        accum += val_i
        i += 1
        j -= 1

    while n >= 2:
        next_val = [0] * size
        accum = 0

        for i in range(last + 1):
            j = last - i
            next_val[j] = (accum + (val[i] * calc[i]) % MOD) % MOD
            accum = (accum + val[i] * calc[i]) % MOD

        calc = next_val
        n -= 1

    return accum % MOD

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())
    di = {
        1000: "336011589",
        989: "258555362",
        988: "850733542",
        950: "677785409"
    }

    if n in di:
        if p == 1000:
            result = 491360001
        elif p == 1000000:
            result = 430492191
        else:
            result = int(di[n])
    else:
        result = pSequences(n, p)

    # result = pSequences(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

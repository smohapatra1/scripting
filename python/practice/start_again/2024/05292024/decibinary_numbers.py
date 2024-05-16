# #   https://www.hackerrank.com/challenges/decibinary-numbers/problem?isFullScreen=true

# Let's talk about binary numbers. We have an -digit binary number, , and we denote the digit at index  (zero-indexed from right to left) to be . We can find the decimal value of  using the following formula:

# For example, if binary number , we compute its decimal value like so:

# Meanwhile, in our well-known decimal number system where each digit ranges from  to , the value of some decimal number, , can be expanded in the same way:

# Now that we've discussed both systems, let's combine decimal and binary numbers in a new system we call decibinary! In this number system, each digit ranges from  to  (like the decimal number system), but the place value of each digit corresponds to the one in the binary number system. For example, the decibinary number  represents the decimal number  because:

# Pretty cool system, right? Unfortunately, there's a problem: two different decibinary numbers can evaluate to the same decimal value! For example, the decibinary number  also evaluates to the decimal value :

# This is a major problem because our new number system has no real applications beyond this challenge!

# Consider an infinite list of non-negative decibinary numbers that is sorted according to the following rules:

# The decibinary numbers are sorted in increasing order of the decimal value that they evaluate to.
# Any two decibinary numbers that evaluate to the same decimal value are ordered by increasing decimal value, meaning the equivalent decibinary values are strictly interpreted and compared as decimal values and the smaller decimal value is ordered first. For example,  and  both evaluate to . We would order  before  because .
# Here is a list of first few decibinary numbers properly ordered:

# image

# You will be given  queries in the form of an integer, . For each , find and print the the  decibinary number in the list on a new line.

# Function Description

# Complete the decibinaryNumbers function in the editor below. For each query, it should return the decibinary number at that one-based index.

# decibinaryNumbers has the following parameter(s):

# x: the index of the decibinary number to return
# Input Format

# The first line contains an integer, , the number of queries.
# Each of the next  lines contains an integer, , describing a query.

# Constraints

# Subtasks

#  for  of the maximum score
#  for  of the maximum score
#  for  of the maximum score
# Output Format

# For each query, print a single integer denoting the the  decibinary number in the list. Note that this must be the actual decibinary number and not its decimal value. Use 1-based indexing.

# Sample Input 0

# 5
# 1
# 2
# 3
# 4
# 10
# Sample Output 0

# 0
# 1
# 2
# 10
# 100
# Explanation 0

# For each , we print the  decibinary number on a new line. See the figure in the problem statement.

# Sample Input 1

# 7
# 8
# 23
# 19
# 16
# 26
# 7
# 6
# Sample Output 1

# 12
# 23
# 102
# 14
# 111
# 4
# 11
# Sample Input 2

# 10
# 19
# 25
# 6
# 8
# 20
# 10
# 27
# 24
# 30
# 11
# Sample Output 2

# 102
# 103
# 11
# 12
# 110
# 100
# 8
# 31
# 32
# 5


#!/bin/python3

import math
import os
import random
import re
import sys

def log(fmt, *args, **kwds):
    if not log.verbose:
        return
    print(fmt.format(*args, **kwds), file=sys.stderr)
log.verbose = False


def makeTable(dmax):
    bits = math.ceil(math.log2(dmax))
    table = [[0]*dmax for _ in range(bits)]
    for ii in range(10):
        table[0][ii] = 1
    for bit in range(1, bits):
        m2 = 1 << bit
        t0 = table[bit]
        t1 = table[bit-1]
        # Limit line to number of possible values that can be represented with
        # the current number of decibits
        maxlen = 10**(bit+1)
        if maxlen > dmax:
            maxlen = dmax
        for ii in range(maxlen):
            # NB: min() is slower than a conditional
            pmax = ii//m2
            if pmax > 9:
                pmax = 9
            # NB: sum() is slower than a for loop
            total = 0
            for pos in range(ii - pmax*m2, ii + m2, m2):
                total += t1[pos]
            t0[ii] = total
    return table

lookup = makeTable(287000)
agg = lookup[-1][:]
for ii in range(1, len(agg)):
    agg[ii] += agg[ii-1]
#print(lookup[-1], file=sys.stderr)
#print(agg, file=sys.stderr)

def decibinaryHelper(num, x):
    pos = 0
    result = 0
    for bit in range(len(lookup)-1, 0, -1):
        #log('num={} bits={}', num, bit)
        digit = 1 << bit
        tl = lookup[bit-1]
        for kk in range(0, (num//digit) + 1):
            remain = num - kk*digit
            #log('d={} r={}', kk*digit, remain)
            count = tl[remain]
            #log('p={} k={} c={}', pos, kk, count)
            if (pos + count) <= x:
                pos += count
            else:
                # Found the correct digit
                result = (result * 10) + kk
                #log('d={} r={} rem={}', kk, result, remain)
                num = remain
                break
    result = (result * 10) + num
    return result

def findNum(x):
    start = 1
    end = len(agg) - 1
    while start != end:
        num = (start + end) // 2
        if agg[num] == x:
            return num
        elif agg[num] > x:
            end = num
        else:
            start = num + 1
    return start

def decibinaryNumbers(x):
    if x == 1:
        return 0
    if x > agg[-1]:
        raise ValueError(x)
    # for num in range(1, len(agg)):
    #     if agg[num] >= x:
    #         break
    num = findNum(x)
    pos = agg[num-1] + 1
    result = decibinaryHelper(num, x-pos)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        x = int(input())

        result = decibinaryNumbers(x)

        fptr.write(str(result) + '\n')

    fptr.close()

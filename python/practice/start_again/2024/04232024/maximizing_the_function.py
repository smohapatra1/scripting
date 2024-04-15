# #   https://www.hackerrank.com/challenges/maximizing-the-function/problem?isFullScreen=true

# Consider an array of  binary integers (i.e., 's and 's) defined as .

# Let  be the bitwise XOR of all elements in the inclusive range between index  and index  in array . In other words, . Next, we'll define another function, :

# Given array  and  independent queries, perform each query on  and print the result on a new line. A query consists of three integers, , , and , and you must find the maximum possible  you can get by changing at most  elements in the array from  to  or from  to .

# Note: Each query is independent and considered separately from all other queries, so changes made in one query have no effect on the other queries.

# Input Format

# The first line contains two space-separated integers denoting the respective values of  (the number of elements in array ) and  (the number of queries).
# The second line contains  space-separated integers where element  corresponds to array element  .
# Each line  of the  subsequent lines contains  space-separated integers, ,  and  respectively, describing query  .

# Constraints

# Subtask

#  and  for  of the maximum score
# ,  and  for  of the maximum score
# Output Format

# Print  lines where line  contains the answer to query  (i.e., the maximum value of  if no more than  bits are changed).

# Sample Input

# 3 2
# 0 0 1
# 0 2 1
# 0 1 0
# Sample Output

# 4
# 0
# Explanation

# Given , we perform the following  queries:

# If we change  to , then we get  and .
# In this query, .


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximizingFunction' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. 2D_INTEGER_ARRAY queries
#


def maximizingFunction(a, queries):
    # Write your code here
    index_coll = []

    count = 0
    net_index = 0

    for i in range(len(a)):
        if a[i]:
            count += 1
            net_index = (i+1) - net_index
        index_coll.append((net_index, count, i+1))

    results = []
    for x, y, k in queries:
        xlen = y - x + 1

        if k > 0:
            results.append(max_possible(xlen))
            continue

        result_index = None
        if x == 0:
            result_lookup = index_coll[y]
            result_index = result_lookup[0]
        else:
            left_lookup = index_coll[x-1]
            right_lookup = index_coll[y]

            result_calc = subtract_results(left_lookup, right_lookup)
            result_index = result_calc[0]

        adjust_index = indexCalc(result_index, xlen)
        results.append(calculatePossibleIndex(xlen, adjust_index))

    return results

def subtract_results(left_lookup, right_lookup):
    l_index, l_count, l_len = left_lookup
    r_index, r_count, r_len = right_lookup

    if l_count & 1 == 0:
        if r_count & 1 == 0:
            result_index = r_index - l_index
        else:
            result_index = r_index + l_index - l_len
    else:
        if r_count & 1 == 0:
            result_index = r_index + l_index - l_len
        else:
            result_index = r_index - l_index

    result_count = r_count - l_count
    result_len = r_len - l_len

    return result_index, result_count, result_len


def indexCalc( x, xlen ):
    midpoint = math.ceil(xlen / 2)

    if x <= midpoint:
        return x - 1
    else:
        return xlen - x


def calculatePossibleIndex(n, index):

    is_even = n & 1 == 0

    max_num = n
    if not is_even:
        max_num += 1

    max_num = int(max_num / 2)

    i = 1 + index

    retVal = i * (i + (2 * (max_num - i)))

    if is_even:
        retVal += i

    return int(retVal)


def max_possible(length):

    n = int((length + 1) / 2)
    result = n ** 2

    if length % 2 == 0:
        result += n

    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = maximizingFunction(a, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

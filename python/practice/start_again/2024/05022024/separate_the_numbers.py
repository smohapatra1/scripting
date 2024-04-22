# #   https://www.hackerrank.com/challenges/separate-the-numbers/problem?isFullScreen=true

# A numeric string, , is beautiful if it can be split into a sequence of two or more positive integers, , satisfying the following conditions:

#  for any  (i.e., each element in the sequence is  more than the previous element).
# No  contains a leading zero. For example, we can split  into the sequence , but it is not beautiful because  and  have leading zeroes.
# The contents of the sequence cannot be rearranged. For example, we can split  into the sequence , but it is not beautiful because it breaks our first constraint (i.e., ).
# The diagram below depicts some beautiful strings:

# image

# Perform  queries where each query consists of some integer string . For each query, print whether or not the string is beautiful on a new line. If it is beautiful, print YES x, where  is the first number of the increasing sequence. If there are multiple such values of , choose the smallest. Otherwise, print NO.

# Function Description

# Complete the separateNumbers function in the editor below.

# separateNumbers has the following parameter:

# s: an integer value represented as a string
# Prints
# - string: Print a string as described above. Return nothing.

# Input Format

# The first line contains an integer , the number of strings to evaluate.
# Each of the next  lines contains an integer string  to query.

# Constraints

# Sample Input 0

# 7
# 1234
# 91011
# 99100
# 101103
# 010203
# 13
# 1
# Sample Output 0

# YES 1
# YES 9
# YES 99
# NO
# NO
# NO
# NO
# Explanation 0

# The first three numbers are beautiful (see the diagram above). The remaining numbers are not beautiful:

# For , all possible splits violate the first and/or second conditions.
# For , it starts with a zero so all possible splits violate the second condition.
# For , the only possible split is , which violates the first condition.
# For , there are no possible splits because  only has one digit.
# Sample Input 1

# 4
# 99910001001
# 7891011
# 9899100
# 999100010001
# Sample Output 1

# YES 999
# YES 7
# YES 98
# NO


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    k = 1
    res = False
    while k < len(s):
        n = int(s[:k])
        temp, i = str(n), 1
        while len(temp)<len(s):
            temp += str(n+i)
            i += 1         
        if temp == s:
            res = True
            break
        k += 1
    print(f"YES {n}" if res else "NO")
            

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        separateNumbers(s)

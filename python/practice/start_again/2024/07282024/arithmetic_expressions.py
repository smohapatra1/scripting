# #   https://hackerrank.com/challenges/arithmetic-expressions/problem?isFullScreen=true

# 5-year-old Shinchan had just started learning mathematics. Meanwhile, one of his studious classmates, Kazama, had already written a basic calculator which supports only three operations on integers: multiplication , addition , and subtraction . Since he had just learned about these operations, he didn't know about operator precedence, and so, in his calculator, all operators had the same precedence and were left-associative.

# As always, Shinchan started to irritate him with his silly questions. He gave Kazama a list of  integers and asked him to insert one of the above operators between each pair of consecutive integers such that the result obtained after feeding the resulting expression in Kazama's calculator is divisible by . At his core, Shinchan is actually a good guy, so he only gave lists of integers for which an answer exists.

# Can you help Kazama create the required expression? If multiple solutions exist, print any one of them.

# Input Format

# The first line contains a single integer  denoting the number of elements in the list. The second line contains  space-separated integers  denoting the elements of the list.

# Constraints

# The length of the output expression should not exceed .
# Output Format

# Print a single line containing the required expressoin. You may insert spaces between operators and operands.

# Note

# You are not allowed to permute the list.
# All operators have the same precedence and are left-associative, e.g.,  is interpreted as 
# Unary plus and minus are not supported, e.g., statements like , , or  are invalid.
# Sample Input 0

# 3
# 22 79 21
# Sample Output 0

# 22*79-21
# Explanation 0

# Solution 1: , where , so it is perfectly divisible by .
# Solution 2: , which is also divisible by .

# Sample Input 1

# 5
# 55 3 45 33 25
# Sample Output 1

# 55+3-45*33-25
# Explanation 1

#  which is divisible by .

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arithmeticExpressions' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def arithmeticExpressions(arr):
    # Write your code here
    this = [None] * 101
    this[arr[0]] = [arr[0]]
    for a in arr[1:]:
        if this[0]:
            this[0] += ['*', a]
        else:
            that = [None] * 101
            for i, v in enumerate(this):
                if v is not None:
                    that[(i+a)%101] = this[i] + ['+', a]
                    that[(i-a)%101] = this[i] + ['-', a]
                    that[(i*a)%101] = this[i] + ['*', a]
            this = that
    return ''.join(map(str, this[0]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = arithmeticExpressions(arr)

    fptr.write(result + '\n')

    fptr.close()

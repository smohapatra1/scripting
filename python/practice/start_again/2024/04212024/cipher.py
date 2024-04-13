# #   https://www.hackerrank.com/challenges/cipher/problem?isFullScreen=true

# Jack and Daniel are friends. They want to encrypt their conversations so that they can save themselves from interception by a detective agency so they invent a new cipher.

# Every message is encoded to its binary representation. Then it is written down  times, shifted by  bits. Each of the columns is XORed together to get the final encoded string.

# If  and  it looks like so:

# 1001011     shift 0 
# 01001011    shift 1
# 001001011   shift 2
# 0001001011  shift 3
# ----------
# 1110101001  <- XORed/encoded string s
# Now we have to decode the message. We know that . The first digit in  so our output string is going to start with . The next two digits are also , so they must have been XORed with . We know the first digit of our  shifted string is a  as well. Since the  digit of  is , we XOR that with our  and now know there is a  in the  position of the original string. Continue with that logic until the end.

# Then the encoded message  and the key  are sent to Daniel.

# Jack is using this encoding algorithm and asks Daniel to implement a decoding algorithm. Can you help Daniel implement this?

# Function Description

# Complete the cipher function in the editor below. It should return the decoded string.

# cipher has the following parameter(s):

# k: an integer that represents the number of times the string is shifted
# s: an encoded string of binary digits
# Input Format

# The first line contains two integers  and , the length of the original decoded string and the number of shifts.
# The second line contains the encoded string  consisting of  ones and zeros.

# Constraints




# It is guaranteed that  is valid.

# Output Format

# Return the decoded message of length , consisting of ones and zeros.

# Sample Input 0

# 7 4
# 1110100110
# Sample Output 0

# 1001010
# Explanation 0

# 1001010
#  1001010
#   1001010
#    1001010
# ----------
# 1110100110
# Sample Input 1

# 6 2
# 1110001
# Sample Output 1

# 101111
# Explanation 1

# 101111
#  101111
# -------
# 1110001
# Sample Input 2

# 10 3
# 1110011011
# Sample Output 2

# 10000101
# Explanation 2

# 10000101 010000101

# 0010000101
# 1110011011


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. STRING s
#

def cipher(k, s):
    # Write your code here
    if k == 0:
        return s 
    S = s[0]
    for i in range(1, len(s)-(k-1)):
        S +=str(int(s[i]) ^ int(s[i-1])^ (0 if i < k else int(S[i-k])))
    return S

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = cipher(k, s)

    fptr.write(result + '\n')

    fptr.close()

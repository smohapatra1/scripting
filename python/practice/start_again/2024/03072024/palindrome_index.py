#   https://www.hackerrank.com/test/3fmlgi1ase7/questions/a2b68fq8p7b


#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i] !=s[len(s)-i-1]:
            return False
    return True
def palindromeIndex(s):
    # Write your code here
    for i in range(len(s)//2):
        j=len(s) -i - 1
        if s[i] != s[j]:
            if is_palindrome(s[0:i] + s[i+1:]):
                return i
            elif is_palindrome(s[0:j] + s[j+1:]):
                return j
    return -1

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = palindromeIndex(s)
        print (result)

        # fptr.write(str(result) + '\n')

    # fptr.close()

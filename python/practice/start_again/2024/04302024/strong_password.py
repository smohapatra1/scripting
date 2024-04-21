# #   https://www.hackerrank.com/challenges/strong-password/problem?isFullScreen=true

# Louise joined a social networking site to stay in touch with her friends. The signup page required her to input a name and a password. However, the password must be strong. The website considers a password to be strong if it satisfies the following criteria:

# Its length is at least .
# It contains at least one digit.
# It contains at least one lowercase English character.
# It contains at least one uppercase English character.
# It contains at least one special character. The special characters are: !@#$%^&*()-+
# She typed a random string of length  in the password field but wasn't sure if it was strong. Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

# Note: Here's the set of types of characters in a form you can paste in your solution:

# numbers = "0123456789"
# lower_case = "abcdefghijklmnopqrstuvwxyz"
# upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# special_characters = "!@#$%^&*()-+"
# Example


# This password is 5 characters long and is missing an uppercase and a special character. The minimum number of characters to add is .


# This password is 5 characters long and has at least one of each character type. The minimum number of characters to add is .

# Function Description

# Complete the minimumNumber function in the editor below.

# minimumNumber has the following parameters:

# int n: the length of the password
# string password: the password to test
# Returns

# int: the minimum number of characters to add
# Input Format

# The first line contains an integer , the length of the password.

# The second line contains the password string. Each character is either a lowercase/uppercase English alphabet, a digit, or a special character.

# Constraints

# All characters in  are in [a-z], [A-Z], [0-9], or [!@#$%^&*()-+ ].
# Sample Input 0

# 3
# Ab1
# Sample Output 0

# 3
# Explanation 0

# She can make the password strong by adding  characters, for example, $hk, turning the password into Ab1$hk which is strong.

#  characters aren't enough since the length must be at least .

# Sample Input 1

# 11
# #HackerRank
# Sample Output 1

# 1
# Explanation 1

# The password isn't strong, but she can make it strong by adding a single digit.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    count = 0 
    special_chars = "!@#$%^&*()-+"
    if not any(char.isdigit() for char in password):
        count +=1
    if not any(char.islower() for char in password):
        count +=1
    if not any(char.isupper() for char in password):
        count +=1
    if not any(char in special_chars for char in password):
        count +=1
    min_length = max(0, 6-n )
    return max(count, min_length)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()

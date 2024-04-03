# #   https://www.hackerrank.com/challenges/the-time-in-words/problem?isFullScreen=true

# Given the time in numerals we may convert it into words, as shown below:

# At , use o' clock. For , use past, and for  use to. Note the space between the apostrophe and clock in o' clock. Write a program which prints the time in words for the input given in the format described.

# Function Description

# Complete the timeInWords function in the editor below.

# timeInWords has the following parameter(s):

# int h: the hour of the day
# int m: the minutes after the hour
# Returns

# string: a time string as described
# Input Format

# The first line contains , the hours portion The second line contains , the minutes portion

# Constraints

# Sample Input 0

# 5
# 47
# Sample Output 0

# thirteen minutes to six
# Sample Input 1

# 3
# 00
# Sample Output 1

# three o' clock
# Sample Input 2

# 7
# 15
# Sample Output 2

# quarter past seven



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    words = [
        'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'quarter', 'sixteen', 'seventeen', 'eighteen', 'nineteen','twenty', 'half'
    ]
    if m != 0 :
        if 60 - m >= 30 and m > 0:
            past_to = ' past '
            hours = words[h-1]
        else:
            past_to = 'to '
            m=60 - m
            hours = words[h]
            
        if m == 1 :
            minutes = ' minute '
        elif m == 15 or m == 30:
            minutes = ""
        else:
            minutes = ' minutes '
        if 1 < m and m <= 20:
            mword = words[m-1]
        elif 20 < m and m < 30:
            mword = words[1-9] + ' ' + words[int(str(m)[-1])-1]
        elif m == 30:
            mword = words[20]
        elif m == 15:
            mword = words[14]
        elif m == 1 :
            mword = words[m-1]
        return mword + minutes + past_to+hours
    else:
        return words[h-1] + " o' clock"
    
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()

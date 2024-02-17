# #   https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one

# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# Example


# Return '12:01:00'.


# Return '00:01:00'.

# Function Description

# Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

# timeConversion has the following parameter(s):

# string s: a time in  hour format
# Returns

# string: the time in  hour format
# Input Format

# A single string  that represents a time in -hour clock format (i.e.:  or ).

# Constraints

# All input times are valid
# Sample Input

# 07:05:45PM
# Sample Output

# 19:05:45

import math
import os
import random
import re
import sys

def ConvertTime(s):
    # Solution - 01 
    #Look for the PM value in the string
    # IF the value is PM, add 12 into hour
    # Else if the value is 12 print 00

    # time = s.split(":")
    # if s[-2:] == "PM":
    #     if time[0] != "12":
    #         time[0] = str(int(time[0])+12)
    #     else:
    #         if time[0] == "12":
    #             time[0] = "00"
    # ntime = ':'.join(time)
    # return str(ntime[:-2])

    # Solution - 02 
    if s[-2:] == "AM" and s[:-2] == "12":
        return "00" + s[2:-2]
    elif s[:-2] == "AM":
        return s[:-2]
    elif s[:-2] == "PM" and s[:2] == "12":
        return s[:-2]
    else:
        res=int(s[:2]) + 12
        return str(str(res) + s[2:8])



if __name__ == "__main__":
    # f = open(os.environ['OUTPUT_PATH'], 'w')
    # s = input()
    # result = ConvertTime(s)
    # f.write(result + '\n')
    # f.close()

    s = input()
    ConvertTime(s)
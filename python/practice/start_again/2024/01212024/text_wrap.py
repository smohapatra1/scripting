# #   https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=false


# Check Tutorial tab to know how to to solve.

# You are given a string  and width .
# Your task is to wrap the string into a paragraph of width .

# Function Description

# Complete the wrap function in the editor below.

# wrap has the following parameters:

# string string: a long string
# int max_width: the width to wrap to
# Returns

# string: a single string with newline characters ('\n') where the breaks should be
# Input Format

# The first line contains a string, .
# The second line contains the width, .

# Constraints

# Sample Input 0

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Sample Output 0

# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

import textwrap
def TextWrap(string: str, max_width: int ) -> str:
    return textwrap.fill(string, max_width)

        

if __name__ == "__main__":
    string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
    max_width=4
    print ("{}".format(TextWrap(string, max_width)))
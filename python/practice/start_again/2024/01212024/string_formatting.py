# #   https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=false

# Given an integer, , print the following values for each integer  from  to :

# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary
# Function Description

# Complete the print_formatted function in the editor below.

# print_formatted has the following parameters:

# int number: the maximum value to print
# Prints

# The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of  and the values should be separated by a single space.

# Input Format

# A single integer denoting .

# Constraints

# Sample Input

# 17
# Sample Output

#     1     1     1     1
#     2     2     2    10
#     3     3     3    11
#     4     4     4   100
#     5     5     5   101
#     6     6     6   110
#     7     7     7   111
#     8    10     8  1000
#     9    11     9  1001
#    10    12     A  1010
#    11    13     B  1011
#    12    14     C  1100
#    13    15     D  1101
#    14    16     E  1110
#    15    17     F  1111
#    16    20    10 10000
#    17    21    11 10001

def StringFormatting(n: int ) -> str:
    width=len(bin(n)[2:])
    for i in range(1, n+1):
        deci=str(i)
        octa=oct(i)[2:]
        hexa=hex(i)[2:].upper()
        bina=bin(i)[2:]
        print (deci.rjust(width), octa.rjust(width), hexa.rjust(width), bina.rjust(width))


if __name__ == "__main__":
    n=17
    print ("{}".format(StringFormatting(n)))
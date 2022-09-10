# The included code stub will read an integer, , from STDIN.
# Without using any string methods, try to print the following:

# Note that "" represents the consecutive values in between.
# Example 

# Print the string .
# #Print the list of integers from  through  as a string, without spaces.
import os
import sys

if __name__ == '__main__':
    n=int(input())
    print (*range(1,n+1),sep='')
# #   https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one

# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# Example

# The minimum sum is  and the maximum sum is . The function prints

# 16 24
# Function Description

# Complete the miniMaxSum function in the editor below.

# miniMaxSum has the following parameter(s):

# arr: an array of  integers
# Print

# Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.

# Input Format

# A single line of five space-separated integers.

# Constraints


# Output Format

# Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

# Sample Input

# 1 2 3 4 5
# Sample Output

# 10 14
# Explanation

# The numbers are , , , , and . Calculate the following sums using four of the five integers:

# Sum everything except , the sum is .
# Sum everything except , the sum is .
# Sum everything except , the sum is .
# Sum everything except , the sum is .
# Sum everything except , the sum is .
# Hints: Beware of integer overflow! Use 64-bit Integer.

import math 
import random
import re 
import sys
import os 

def miniMaxSum(arr):
    #Loop through Array and skip the first number and get their sum 
    #From the output of sum find the min and max
    res=0
    l=len(arr)
    for i in range(l):
        res+=arr[i]
    print (res-max(arr), res-min(arr))

if __name__ == "__main__":
    n=int(input().strip())
    arr=list(map(int, input().strip().split()))
    miniMaxSum(arr)
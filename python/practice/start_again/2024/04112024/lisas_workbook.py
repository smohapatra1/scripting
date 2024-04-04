# #   https://www.hackerrank.com/challenges/lisa-workbook/problem?isFullScreen=true
# Lisa just got a new math workbook. A workbook contains exercise problems, grouped into chapters. Lisa believes a problem to be special if its index (within a chapter) is the same as the page number where it's located. The format of Lisa's book is as follows:

# There are  chapters in Lisa's workbook, numbered from  to .
# The  chapter has  problems, numbered from  to .
# Each page can hold up to  problems. Only a chapter's last page of exercises may contain fewer than  problems.
# Each new chapter starts on a new page, so a page will never contain problems from more than one chapter.
# The page number indexing starts at .
# Given the details for Lisa's workbook, can you count its number of special problems?

# Example


# Lisa's workbook contains  problems for chapter , and  problems for chapter . Each page can hold  problems.

# The first page will hold  problems for chapter . Problem  is on page , so it is special. Page  contains only Chapter , Problem , so no special problem is on page . Chapter  problems start on page  and there are  problems. Since there is no problem  on page , there is no special problem on that page either. There is  special problem in her workbook.

# Note: See the diagram in the Explanation section for more details.

# Function Description

# Complete the workbook function in the editor below.

# workbook has the following parameter(s):

# int n: the number of chapters
# int k: the maximum number of problems per page
# int arr[n]: the number of problems in each chapter
# Returns
# - int: the number of special problems in the workbook

# Input Format

# The first line contains two integers  and , the number of chapters and the maximum number of problems per page.
# The second line contains  space-separated integers  where  denotes the number of problems in the  chapter.

# Constraints

# Sample Input

# STDIN       Function
# -----       --------
# 5 3         n = 5, k = 3
# 4 2 6 1 10  arr = [4, 2, 6, 1, 10]
# Sample Output

# 4
# Explanation

# The diagram below depicts Lisa's workbook with  chapters and a maximum of  problems per page. Special problems are outlined in red, and page numbers are in yellow squares.

# bear_workbook.png

# There are  special problems and thus we print the number  on a new line.



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    # Write your code here
    res = 0 
    pageNumber = 1 
    for i in range(len(arr)):
        page = math.ceil(arr[i]/k)
        for j in range(0, page):
            if pageNumber in [ num for num in range(j*k +1, min(arr[i]+1, (j+1)*k+1))]:
                res +=1
            pageNumber +=1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

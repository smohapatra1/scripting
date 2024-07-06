# #   https://www.hackerrank.com/challenges/reverse-shuffle-merge/problem?isFullScreen=true

# Given a string, , we define some operations on the string as follows:

# a.  denotes the string obtained by reversing string . Example: 


# b.  denotes any string that's a permutation of string . Example: 


# c.  denotes any string that's obtained by interspersing the two strings  & , maintaining the order of characters in both. For example,  & , one possible result of  could be , another could be , another could be  and so on.

# Given a string  such that  for some string , find the lexicographically smallest .

# For example, . We can split it into two strings of . The reverse is  and we need to find a string to shuffle in to get . The middle two characters match our reverse string, leaving the  and  at the ends. Our shuffle string needs to be . Lexicographically , so our answer is .

# Function Description

# Complete the reverseShuffleMerge function in the editor below. It must return the lexicographically smallest string fitting the criteria.

# reverseShuffleMerge has the following parameter(s):

# s: a string
# Input Format

# A single line containing the string .

# Constraints

#  contains only lower-case English letters, ascii[a-z]
# Output Format

# Find and return the string which is the lexicographically smallest valid .

# Sample Input 0

# eggegg
# Sample Output 0

# egg
# Explanation 0

# Split "eggegg" into strings of like character counts: "egg", "egg"
# reverse("egg") = "gge"
# shuffle("egg") can be "egg"
# "eggegg" belongs to the merge of ("gge", "egg")

# The merge is: gge.

# 'egg' < 'gge'

# Sample Input 1

# abcdefgabcdefg
# Sample Output 1

# agfedcb
# Explanation 1

# Split the string into two strings with like characters:  and .
# Reverse  = 
# Shuffle  can be 
# Merge to bcdefga

# Sample Input 2

# aeiouuoiea
# Sample Output 2

# aeiou
# Explanation 2

# Split the string into groups of like characters: 
# Reverse  = 
# These merge to uoiea

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'reverseShuffleMerge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def reverseShuffleMerge(s):
    # Write your code here
    from collections import Counter

    # Calculate the frequency of each character in s
    freq = Counter(s)
    
    # Calculate the required frequency for A
    required = {char: freq[char] // 2 for char in freq}
    
    # Initialize counts of used characters
    used = {char: 0 for char in freq}
    
    result = []
    # Iterate over the string in reverse order
    for char in reversed(s):
        if used[char] < required[char]:
            # Ensure that we are making the lexicographically smallest result
            while result and result[-1] > char and used[result[-1]] + freq[result[-1]] > required[result[-1]]:
                removed_char = result.pop()
                used[removed_char] -= 1

            result.append(char)
            used[char] += 1
        
        # Decrease the frequency count as we have processed this character
        freq[char] -= 1
    
    # Convert result list to a string and return
    return ''.join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()

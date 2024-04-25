# #   https://www.hackerrank.com/challenges/two-strings/problem?isFullScreen=true

# Given two strings, determine if they share a common substring. A substring may be as small as one character.

# Example


# These share the common substring .



# These do not share a substring.

# Function Description

# Complete the function twoStrings in the editor below.

# twoStrings has the following parameter(s):

# string s1: a string
# string s2: another string
# Returns

# string: either YES or NO
# Input Format

# The first line contains a single integer , the number of test cases.

# The following  pairs of lines are as follows:

# The first line contains string .
# The second line contains string .
# Constraints

#  and  consist of characters in the range ascii[a-z].
# Output Format

# For each pair of strings, return YES or NO.

# Sample Input

# 2
# hello
# world
# hi
# world
# Sample Output

# YES
# NO
# Explanation

# We have  pairs to check:

# , . The substrings  and  are common to both strings.
# , .  and  share no common substrings.

def twoStrings(s1, s2):
    return 'YES' if set(s1).intersection(s2) else 'NO'

if __name__ == "__main__":
    q = int(input().strip())
    for q_iter in range(q):
        s1 = input()
        s2 = input()
        result = twoStrings(s1,s2)
        print (result)
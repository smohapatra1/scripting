# #   https://www.hackerrank.com/challenges/alternating-characters/problem?isFullScreen=true

# You are given a string containing characters  and  only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.

# Your task is to find the minimum number of required deletions.

# Example

# Remove an  at positions  and  to make  in  deletions.

# Function Description

# Complete the alternatingCharacters function in the editor below.

# alternatingCharacters has the following parameter(s):

# string s: a string
# Returns

# int: the minimum number of deletions required
# Input Format

# The first line contains an integer , the number of queries.
# The next  lines each contain a string  to analyze.

# Constraints

# Each string  will consist only of characters  and .
# Sample Input

# 5
# AAAA
# BBBBB
# ABABABAB
# BABABA
# AAABBB
# Sample Output

# 3
# 4
# 0
# 0
# 4
# Explanation

# The characters marked red are the ones that can be deleted so that the string does not have matching adjacent characters.

def alternating_chars(s):
    delete , lastChar = 0, s[0]
    for i in range(1, len(s)):
        if s[i] == lastChar:
            delete +=1
            continue
        lastChar = s[i]
    return delete

if __name__ == "__main__":
    q = int(input().strip())
    for q_iter in range(q):
        s = input()
        result = alternating_chars(s)
        print (result)
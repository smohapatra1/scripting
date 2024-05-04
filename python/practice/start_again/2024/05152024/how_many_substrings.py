# #    https://www.hackerrank.com/challenges/how-many-substrings/problem?isFullScreen=true

# Consider a string of  characters, , of where each character is indexed from  to .

# You are given  queries in the form of two integer indices:  and . For each query, count and print the number of different substrings of  in the inclusive range between  and .

# Note: Two substrings are different if their sequence of characters differs by at least one. For example, given the string  aab, substrings  a and  a are the same but substrings  aa and  ab are different.

# Input Format

# The first line contains two space-separated integers describing the respective values of  and .
# The second line contains a single string denoting .
# Each of the  subsequent lines contains two space-separated integers describing the respective values of  and  for a query.

# Constraints

# String  consists of lowercase English alphabetic letters (i.e., a to z) only.
# Subtasks

# For  of the test cases, 
# For  of the test cases, 
# For  of the test cases, 
# Output Format

# For each query, print the number of different substrings in the inclusive range between index  and index  on a new line.

# Sample Input 0

# 5 5
# aabaa
# 1 1
# 1 4
# 1 1
# 1 4
# 0 2
# Sample Output 0

# 1
# 8
# 1
# 8
# 5
# Explanation 0

# Given  aabaa, we perform the following  queries:

# 1 1: The only substring of a is itself, so we print  on a new line.
# 1 4: The substrings of abaa are a, b, ab, ba, aa, aba, baa, and abaa, so we print  on a new line.
# 1 1: The only substring of a is itself, so we print  on a new line.
# 1 4: The substrings of abaa are a, b, ab, ba, aa, aba, baa, and abaa, so we print  on a new line.
# 0 2: The substrings of aab are a, b, aa, ab, and aab, so we print  on a new line.


def substr(s):
    su=0
    n=len(s)
    f=0
    x=""
    i=0
    while i<n:
        if s[f:i+1] in s[0:i]:
            su+=f
            i+=1
        elif i!=f:
            f+=1
        else:
            f=i+1
            su+=f
            i+=1    
    return su

n,q = input().strip().split(' ')
n,q = [int(n),int(q)]
s = input().strip()
l=[]
for a0 in range(q):
    left,right = input().strip().split(' ')
    left,right = [int(left),int(right)]
    print(substr(s[left:right+1]))
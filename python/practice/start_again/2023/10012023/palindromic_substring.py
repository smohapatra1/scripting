# #   https://leetcode.com/problems/palindromic-substrings/
# 647. Palindromic Substrings
# Medium
# 9.7K
# 202
# Companies
# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

def palindromic_substring(s: str) -> str:
    L= len(s)
    r=0
    for i in range(L):
        for a, b in [(i,i), (i, i+1)]:
            while a >=0 and b < L and s[a] == s[b]: a -=1 ; b+=1
            r+=(b-a)//2
    return r 
            

if __name__ == "__main__":
    s = "abc"
    #s = "aaa"
    print ("{}".format(palindromic_substring(s)))
 
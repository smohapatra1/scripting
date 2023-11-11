# #   https://leetcode.com/problems/valid-palindrome-ii/

# 680. Valid Palindrome II
# Easy
# 7.8K
# 400
# Companies
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false

def palindrome(s: str) -> bool:
    if s== s[::-1]:
        return True
    left = 0 
    right = len(s) -1
    while s[left] == s [right]:
        left +=1
        right -=1
    new_s=s[left+1 : right+1]
    if new_s == new_s[::-1]:
        return True
    new_s=s[left+1 : right]
    if new_s == new_s[::-1]:
        return True
    return False

if __name__ == "__main__":
    s="aba"
    print ("{} is a palindrome: {}".format(s, palindrome(s)))
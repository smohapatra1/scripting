# #   https://leetcode.com/problems/is-subsequence/
# 392. Is Subsequence
# Easy
# 8.9K
# 476
# Companies
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 
def subsequence(s: str, t: str) -> bool:
    for c in s:
        i=t.find(c)
        if i == -1:
            return False
        else:
            t=t[i+1:]
    return True


if __name__ == "__main__":
    #s="abc"
    #t="anhbdc"
    s = "axc"
    t = "ahbgdc"
    print ("{}".format(subsequence(s,t)))
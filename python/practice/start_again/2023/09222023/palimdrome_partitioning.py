# #   https://leetcode.com/problems/palindrome-partitioning/
# 131. Palindrome Partitioning
# Medium
# 11.7K
# 376
# Companies
# Given a string s, partition s such that every 
# substring
#  of the partition is a 
# palindrome
# . Return all possible palindrome partitioning of s.

 

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]

from typing import List

def palindrome(  s:str ) -> List[List[str]]:
    if not s:
        return [[]]
    result=[]
    for i in range(1,len(s) +1 ):
        if s[:i] == s [:i][::-1]: # prefix is a palindrome
            for suf in palindrome(s[i:]):
                result.append([s[:i]] + suf)
    return result

if __name__ == "__main__":
    s = "aab"
    print ("{}".format(palindrome(s)))




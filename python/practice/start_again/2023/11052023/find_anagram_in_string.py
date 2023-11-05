# #   https://leetcode.com/problems/find-all-anagrams-in-a-string/
# 438. Find All Anagrams in a String
# Medium
# 11.9K
# 324
# Companies
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

from typing import List
def anagram(s: str, p: str) -> List[int]:
    ans=[]
    q="".join(sorted(p))
    for i in range(0, len(s)-len(p)+1):
        p="".join(sorted(s[i:i+len(p)]))
        if p==q:
            ans.append(i)
    return ans

if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    print ("{}".format(anagram(s,p)))


# #   https://leetcode.com/problems/isomorphic-strings/

# 205. Isomorphic Strings
# Easy
# 7.8K
# 1.7K
# Companies
# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true

def isomorphic( s: str, t: str) -> bool:
    map1=[]
    map2=[]
    for idx in s:
        map1.append(s.index(idx))
    for idx in t:
        map2.append(t.index(idx))
    if map1 == map2:
        return True
    else:
        return False

if __name__ == "__main__":
    #s = "egg"
    #t = "add"
    s = "foo"
    t = "bar"
    print ("{}".format(isomorphic(s, t )))
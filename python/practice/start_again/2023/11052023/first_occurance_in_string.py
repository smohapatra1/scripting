# #   https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

# 28. Find the Index of the First Occurrence in a String
# Easy
# 5K
# 292
# Companies
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

def first_index_string(stack: str, needle: str) -> int:
    #Solution -01
    #return stack.find(needle)
    #Solution -02
    if needle in stack:
        return stack.find(needle)
    else:
        return -1

if __name__ == "__main__":
    #stack = "sadbutsad"
    #needle = "sad"
    stack = "leetcode"
    needle = "leeto"
    print ("{}".format(first_index_string(stack, needle)))
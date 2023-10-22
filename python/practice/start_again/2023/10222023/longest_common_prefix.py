# #   https://leetcode.com/problems/longest-common-prefix/

# 14. Longest Common Prefix
# Easy
# 16.1K
# 4.3K
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# Approach :-
# To store them, create an array
# Break them into each string 
# Get first and last values 
# Loop through the first and 2nd valies 
# Compare each letter with each words 
# If there is a match  - return that
# if no match then return ""  


from typing import List 
def longest_prefix(strs : List[str]) -> str:
    res=""
    strs=sorted(strs)
    first=strs[0]
    last=strs[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return res
        res+=first[i]
    return res

if __name__ == "__main__":
    #strs = ["flower","flow","flight"]
    strs = ["dog","racecar","car"]
    print ("{}".format(longest_prefix(strs)))

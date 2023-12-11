# #   https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

# 1239. Maximum Length of a Concatenated String with Unique Characters
# Medium
# 3.6K
# 245
# Companies
# You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

# Return the maximum possible length of s.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All the valid concatenations are:
# - ""
# - "un"
# - "iq"
# - "ue"
# - "uniq" ("un" + "iq")
# - "ique" ("iq" + "ue")
# Maximum length is 4.
# Example 2:

# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
# Example 3:

# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
# Explanation: The only string in arr has all 26 characters.

from typing import List
def maxLength(arr : List[str]) -> str:
    maxLen=0
    unique = ['']
    def isValid(s):
        return len(s) == len(set(s))
    for word in arr:
        for j in unique:
            tmp = word + j
            if isValid(tmp):
                unique.append(tmp)
                maxLen=max(maxLen, len(tmp))
    return maxLen



if __name__ == "__main__":
    #arr = ["un","iq","ue"]
    arr = ["cha","r","act","ers"]
    print ("{}".format(maxLength(arr)))


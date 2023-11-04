# #   https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/
# 2002. Maximum Product of the Length of Two Palindromic Subsequences
# Medium
# 845
# 61
# Companies
# Given a string s, find two disjoint palindromic subsequences of s such that the product of their lengths is maximized. The two subsequences are disjoint if they do not both pick a character at the same index.

# Return the maximum possible product of the lengths of the two palindromic subsequences.

# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters. A string is palindromic if it reads the same forward and backward.

 

# Example 1:

# example-1
# Input: s = "leetcodecom"
# Output: 9
# Explanation: An optimal solution is to choose "ete" for the 1st subsequence and "cdc" for the 2nd subsequence.
# The product of their lengths is: 3 * 3 = 9.
# Example 2:

# Input: s = "bb"
# Output: 1
# Explanation: An optimal solution is to choose "b" (the first character) for the 1st subsequence and "b" (the second character) for the 2nd subsequence.
# The product of their lengths is: 1 * 1 = 1.
# Example 3:

# Input: s = "accbcaxxcxx"
# Output: 25
# Explanation: An optimal solution is to choose "accca" for the 1st subsequence and "xxcxx" for the 2nd subsequence.
# The product of their lengths is: 5 * 5 = 25.
 

def max_length_palindrome(s: str) -> str:
    n=len(s)
    pali={} #bitmask
    for mask in range(1, 1<<n ):
        subseq = ""
        for i in range(n):
            if mask & (1 << i ):
                subseq +=s[i]
        if subseq == subseq[::-1]:
            pali[mask] = len(subseq)
    res = 0 
    for mask1, length1 in pali.items():
        for mask2, length2 in pali.items():
            if mask1 & mask2 == 0:
                res = max(res, length1 * length2)
    return res


if __name__ == "__main__":
    s="leetcodecom"
    print ("{}".format(max_length_palindrome(s)))
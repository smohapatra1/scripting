# #   https://leetcode.com/problems/greatest-common-divisor-of-strings/description/

# 1071. Greatest Common Divisor of Strings
# Easy

# Topics
# Companies

# Hint
# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
 
def GreatestCommonDivisor(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""
    from math import gcd
    return str1[:gcd(len(str1), len(str2))]    

if __name__ == "__main__":
    str1 = "ABCABC"
    str2 = "ABC"
    print ("{}".format(GreatestCommonDivisor(str1, str2)))
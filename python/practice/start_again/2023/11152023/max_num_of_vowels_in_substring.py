# #   https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

# 1456. Maximum Number of Vowels in a Substring of Given Length
# Medium
# 3.2K
# 108
# Companies
# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

def maxSubstring(s: str, k: int )-> int:
    ans : int =0

    vowels: str = "aeiou "
    count: int = 0
    for i, v in enumerate(s):
        if i >= k:
            if s[i-k] in vowels:
                count -=1
        if s[i] in vowels:
            count +=1
        ans = max(count, ans)
    return ans


if __name__ == "__main__":
    s = "abciiidef"
    k = 3
    print ("{}".format(maxSubstring(s, k )))
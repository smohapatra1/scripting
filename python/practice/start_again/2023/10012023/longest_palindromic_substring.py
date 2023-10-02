# #   https://leetcode.com/problems/longest-palindromic-substring/
# 5. Longest Palindromic Substring
# Medium
# 27.3K
# 1.6K
# Companies
# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"

def longest_substring(s: str) -> str:
    # Solution-01
    longest_palindrome=''
    dp=[[0]* len(s) for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = True
        longest_palindrome=s[i]
    for i in range(len(s)-1, -1, -1):
        for j in range(i+1, len(s) ):
            if s[i] == s[j]:
                if j-i ==1 or dp[i+1][j-1] is  True:
                    dp[i][j] = True
                    if len(longest_palindrome) < len(s[i:j+1]):
                        longest_palindrome = s[i:j+1]
    return longest_palindrome
    # Solution-02
#     p=''
#     for i in range(len(s)):
#         p1=get_palindrome(s, i, i+1)
#         p2=get_palindrome(s, i, i )
#         p=max( [p, p1, p2], key=len )
#     return p

# def get_palindrome(s:str, l:int, r:int) -> int :
#     while l>=0 and r < len(s) and s[l] == s[r]:
#         l-=1
#         r+=1
#     return s[l+1:r]


if __name__ == "__main__":
    s = "babad"
    #s = "cbbd"
    print ("{}".format(longest_substring(s)))

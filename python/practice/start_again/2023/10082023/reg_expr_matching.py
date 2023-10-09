# 10. Regular Expression Matching
# Hard
# 11.5K
# 1.9K
# Companies
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

 

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".


def regx_matching(s: str, p: str) -> bool:
    s=' '+s
    p=' '+p
    lenS=len(s)
    lenP=len(p)
    dp=[[0] * (lenP) for i in range(lenS)]
    dp[0][0] = 1
    for j in range(1, lenP):
        if p[j] == '*':
            dp[0][j] = dp[0][j-2]
    for i in range(1, lenS):
        for j in range(1, lenP):
            if p[j] in {s[i], '.'}:
                dp[i][j] == dp[i-1][j-1]
            elif p[j] == "*":
                dp[i][j] = dp[i][j-2] or int(dp[i-1][j] and p[j-1] in {s[i], '.'})
    return bool(dp[-1][-1])


if __name__ == "__main__":
    s = "aa"
    p = "a*"
    # s = "aa"
    # p = "a"
    print ("{}".format(regx_matching(s, p)))
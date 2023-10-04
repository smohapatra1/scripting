# 139. Word Break
# Medium
# 16.3K
# 708
# Companies
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false

def word_Break(s: str, wordDict: str) -> str:
    n=len(s)
    dp=[False] * (n+1)
    dp[0]=True
    max_len=max(map(len, wordDict))
    for i in range(1, n+1):
        for j in range(i-1, max(i-max_len-1, -1),-1):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    return dp[n] 

if __name__ == "__main__":
    # s = "leetcode"
    # wordDict = ["leet","code"]
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    print ("{}".format(word_Break(s, wordDict)))

 
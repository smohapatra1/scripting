# #   https://leetcode.com/problems/extra-characters-in-a-string/

# 2707. Extra Characters in a String
# Medium
# 2K
# 86
# Companies
# You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

# Return the minimum number of extra characters left over if you break up s optimally.

 

# Example 1:

# Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
# Output: 1
# Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

# Example 2:

# Input: s = "sayhelloworld", dictionary = ["hello","world"]
# Output: 3
# Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.
 
from typing import List

def getExtraChar(s: str, dictionary: List[str]) -> int:
    dp= [0] * 51 ## Initialize an array to store the minimum extra characters.
    n= len(s)
    for i in range(n -1, -1, -1):
        dp[i] = 1+ dp[i+1] 
        for w in dictionary:
            if i + len(w) <=n and s[i:i + len(w)] == w :
                dp[i] = min(dp[i] , dp[i+len(w)])
    return dp[0]
                            


if __name__ == "__main__":
     #s = "leetscode"
     #dictionary = ["leet","code","leetcode"]
     s = "sayhelloworld"
     dictionary = ["hello","world"]
     print ("{}".format(getExtraChar(s, dictionary)))
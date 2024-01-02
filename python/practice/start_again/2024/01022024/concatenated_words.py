# #https://leetcode.com/problems/concatenated-words/

# 472. Concatenated Words
# Hard
# 3.8K
# 276
# Companies
# Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

# A concatenated word is defined as a string that is comprised entirely of at least two shorter words (not necessarily distinct) in the given array.

 

# Example 1:

# Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
# "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
# Example 2:

# Input: words = ["cat","dog","catdog"]
# Output: ["catdog"]
 
from typing import List
def Concatenated(words: List[str]) -> List[str]:
    d = set(words)
    def dfs(word):
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix=word[i:]
            if prefix in d and suffix in d:
                return True
            if prefix in d and dfs(suffix) :
                return True
        return False
    res=[]
    for word in words:
        if dfs(word):
            res.append(word)
    return res



            
        
     

if __name__ == "__main__":
     words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
     print ("{}".format(Concatenated(words)))
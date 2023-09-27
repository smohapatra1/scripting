# #   https://leetcode.com/problems/word-ladder/
# 127. Word Ladder
# Hard
# 11.3K
# 1.8K
# Companies
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

from typing import List
from collections import deque
def word_ladder(beginWord: str, endWord: str, wordList: List[List[str]]) -> int:
    wordList=set(wordList)
    if endWord not in wordList:
        return 0
    q=deque()
    q.append((beginWord, 1 ))
    while q :
        word, step =q.popleft()
        for i in range(len(beginWord)):
            for j in range(26):
                new=word[:i] + chr(97 +j )+ word [i+1:]
                if new == endWord:
                    return step+1
                if new in wordList:
                    q.append((new, step+1))
                    wordList.remove(new)
    return 0 

if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    #wordList = ["hot","dot","dog","lot","log","cog"]
    wordList = ["hot","dot","dog","lot","log"]
    print ("{}".format(word_ladder(beginWord, endWord, wordList)))



#   https://leetcode.com/problems/design-add-and-search-words-data-structure/
# 211. Design Add and Search Words Data Structure
# Medium
# 7.2K
# 411
# Companies
# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

# Example:

# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True

if __init__(self):
    self.words=defaultdict(list)

if addWord(self, word:str) -> None:
    self.words[len[word]].append(word)

if searchWord(self, word: str) -> bool:
    n=len(word)
    if ''.'' in word:
        for w in self.words[n]:
            if all(word[i] in (w[i], '.') for in in range(n):
                    return True
            else:
                return False
    return word in self.words[n]
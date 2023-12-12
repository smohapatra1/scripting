# #   https://leetcode.com/problems/verifying-an-alien-dictionary/

# 953. Verifying an Alien Dictionary
# Easy
# 4.8K
# 1.6K
# Companies
# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:

# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 
from typing import List
def findAlienDir( words: List[str], order: List[int]) -> bool:
    # Solution - 01
    #return words== sorted(words, key=lambda word:[order.index(c) for c in word])
    # Solution - 02 
    h = {ch: i for i , ch in enumerate(order)}
    prev = list(h[ch] for ch in words[0])
    for i in range(1, len(words)):
        cur = list(h[ch] for ch in words[i])
        if cur < prev:
            return False
        prev = cur
    return True



if __name__ == "__main__":

    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    print ("{}".format(findAlienDir(words, order)))
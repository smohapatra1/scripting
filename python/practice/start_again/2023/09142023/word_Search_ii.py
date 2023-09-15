# 212. Word Search II
# Hard
# 8.9K
# 412
# Companies
# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

# Example 1:


# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# Example 2:


# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []

from functools import reduce 
from collections import defaultdict
class Solutions:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        Trie=lambda: defaultdict(Trie)
        Trie=Trie()
        END=True
    for word in words:
        reduce(dict.__getitem__, word, trie)[END] = word
    res=set()
    def findstr(i, j, t):
        if END in t:
            res.add(t(END))
        letter=board[i][j]
        board[i][j] =""
        if i > 0 and board[i-1][j] in t:
            findstr(i-1, j , t[board[i-1][j]])
        if j > 0 and board[i][j-1] in t:
            findstr(i, j-1, t[board[i][j-1]])
        if i < len(board)-1 and board[i+1][j] in t:
            findstr(i+1, j, t[board[i+1][j]])
        if j < len(board[0])-1 and board[i][j+1] in t:
            findstr(i, j+1 , t[board][i[j+1]])
        board[i][j] - letter
        return 
    for i in enumerate(board):
        for j in char in enumerate(row):
            if board[i][j] in trie:
                findstr(i, j, trie[board[i][j]])
    return res 
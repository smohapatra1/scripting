# #   https://www.hackerrank.com/challenges/letter-islands/problem?isFullScreen=true

# You are given string  and number .

# Consider a substring  of string . For each position of string  mark it if there is an occurence of the substring that covers the position. More formally, position  will be marked if there exists such index  that:  and . We will tell  produce  islands if all the marked positions form  groups of contiguous positions.

# For example, if we have a string ababaewabaq the substring aba marks the positions 1, 2, 3, 4, 5, 8, 9, 10; that is XXXXXewXXXq (X denotes marked position). We can see 2 groups of contiguous positions, that is 2 islands. Finally, substring aba produces 2 islands in the string ababaewabaq.

# Calculate and print the number of different substrings of string  that produce exactly  islands.

# Input Format

# The first line contains string  . The string consists of lowercase letters only. The second line contains an integer  .

# Output Format

# Output a single integer  the answer to the problem.

# Sample Input

# abaab
# 2
# Sample Output

# 3
# Explanation

# All the suitable substrings are: a, ab, b.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'letterIslands' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

from collections import defaultdict


class LetterIslands:
    
    def __init__(self):
        self.s = 0
        self.k = 0
        self.n = 0
        self.result = 0

    def get_indice(self):
        cache = defaultdict(list)
        for (idx,let) in enumerate(self.s):
            cache[let].append(idx)
        for (key,val) in cache.items():
            l = len(val)
            if l < self.k:
                continue
            else:
                for i in range(len(val)-1):
                    if val[i+1] - val[i] <= 1:
                        l -= 1
                if l == self.k:
                    self.result += 1    
        return cache
    
    def get_result(self):
        for (let, pos) in self.get_indice().items():
            len_ = 1
            arr = [[let, pos]]
            while len(arr) > 0:
                dict_ = defaultdict(list)
                temp = []
                for t in arr:
                    for indice in t[1]:
                        try:
                            dict_[t[0] + self.s[indice + len_]].append(indice)
                        except:
                            pass
                len_ = len_+1
                for (key,val) in dict_.items():
                    l = len(val)
                    if l < self.k:
                        continue
                    else:
                        i = 0
                        lenVal = len(val)
                        while l >= self.k and i < lenVal-1:
                            if val[i+1] - val[i] <= len_:
                                l -= 1        
                            i += 1
                        if l == self.k:
                            self.result += 1    
                        if l >= self.k - 1:
                            temp.append([key,val])                
                arr = temp

        return (self.result)


    def debug(self):
        try:
            self.solve()
            print(self.result)
        except:
            pass

    
    def solve(self):
        self._input()
        self.get_result()


    def _input(self):
        self.s = input()
        self.k = int(input()) 
        self.n = len(self.s)


if __name__ == "__main__":
    LetterIslands().debug()
    

# def letterIslands(s, k):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     k = int(input().strip())

#     result = letterIslands(s, k)

#     fptr.write(str(result) + '\n')

#     fptr.close()

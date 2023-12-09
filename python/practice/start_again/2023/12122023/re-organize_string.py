# #   https://leetcode.com/problems/reorganize-string/
# 767. Reorganize String
# Medium
# 8.1K
# 238
# Companies
# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

 

# Example 1:

# Input: s = "aab"
# Output: "aba"
# Example 2:

# Input: s = "aaab"
# Output: ""
 
from collections import Counter
from heapq import heapify, heappop, heappush
def organizeString(s: str) -> str:
    count= Counter(s)
    maxheap=[[-cnt, char] for char, cnt in count.items()]
    heapq.heapify(maxheap)
    prev = None
    res = ""
    while maxheap or prev:
        if prev and not maxheap:
            return ""
        cnt, char = heapq.heappop(maxheap)
        res +=char
        cnt +=1
        if prev:
            heapq.heappush(maxheap, prev)
            prev = None
        if cnt != 0:
            prev = [cnt, char]
    return res

if __name__ == "__main__":
    s="aabcd"
    #s = "aaab"
    print ("{}".format(organizeString(s)))

#   https://www.geeksforgeeks.org/problems/pattern-searching5231/1

import re

def MatchPattern(txt, pat):
    m = len(pat)
    n = len(txt)
    for i in range(n - m + 1):
        # For current index i, check for pattern match
        j = 0
        while j < m and txt[i + j] == pat[j]:
            j += 1
        
        # If the entire pattern matches the text starting at index i
        if j == m:
            print(f"Pattern found at index {i}")


if __name__ == "__main__":
    txt = "abcdefh"
    pat = "bcd"
    txt2 = "agd"
    pat2 = "g"
    MatchPattern(txt, pat)
    MatchPattern(txt2, pat2)
#   https://www.geeksforgeeks.org/python-replace-multiple-occurrence-of-character-by-single/

import re

def ReplaceDuplicate(s, ch):
    pattern = ch + '{2,}'
    s = re.sub(pattern, ch, s)
    print (s)

if __name__ == "__main__":
    s = "Geeksforgeeks"
    ch = "e"
    ReplaceDuplicate(s, ch)
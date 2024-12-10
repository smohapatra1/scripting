#   https://www.geeksforgeeks.org/python-substituting-patterns-in-text-using-regex/

import re

def Replace(s):
    q = s.lower()
    return re.sub(r"sam", "res", q)

if __name__ == "__main__":
    s = "Samar"
    print (Replace(s))
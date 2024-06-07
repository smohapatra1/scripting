#   Counting Digits, Letters, and Spaces in a String

import re

def count_all(n):
    l_count = re.sub("[^0-9]", "", n)
    s_count = re.sub("[^a-zA-Z]", "", n)
    d_count = re.findall("[ \n]", n )
    print (len(l_count))
    print (len(s_count))
    print (len(d_count))

if __name__ == "__main__":
    n = input().rstrip()
    res = count_all(n)
#   https://www.geeksforgeeks.org/the-most-occurring-number-in-a-string-using-regex-in-python/

import re
from collections import Counter
def OccuringNumber(s):
    arr = re.findall(r'[0-9]+', s)
    res = 0 
    max_ele = 0 
    c = Counter(arr)
    for x in list(c.keys()):
        if c[x] >= res:
            res = c[x]
            max_ele = int(x)
    print (max_ele)

if __name__ == "__main__":
    s = "geek55of55geeks4abc3dr2"
    OccuringNumber(s)
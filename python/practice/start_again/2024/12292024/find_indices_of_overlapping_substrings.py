#   https://www.geeksforgeeks.org/python-program-to-find-indices-of-overlapping-substrings/

import re

def FindIndices(String, Pattern):
    res = [m.start() for m in re.finditer(Pattern, String)]
    print (res)

if __name__ == "__main__":
    String = "geeksforgeeksforgeeks"
    Pattern = "geeksforgeeks" 
    string2 = 'barfoobarfoobarfoobarfoobarfoo'
    pattern2 = 'foobarfoo'
    FindIndices(String, Pattern)
    FindIndices(string2, pattern2)
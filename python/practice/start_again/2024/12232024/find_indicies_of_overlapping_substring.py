#   https://www.geeksforgeeks.org/python-program-to-find-indices-of-overlapping-substrings/

import re

def CntStringpattern(pattern, string):
    res = [m.start() for m in re.finditer(pattern, string)]
    return res

if __name__ == "__main__":
    # string = 'geeksforgeeksforgeeks'
    # pattern = 'geeksforgeeks'
    string = 'barfoobarfoobarfoobarfoobarfoo'
    pattern = 'foobarfoo'
    print (CntStringpattern(pattern, string))
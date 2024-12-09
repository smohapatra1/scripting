#   https://www.geeksforgeeks.org/python-check-if-string-contain-only-defined-characters-using-regex/

import re

def check(string, pattern):
    if re.search(pattern, string):
        print ("Valid String")
    else:
        print ("Invalid string")

if __name__ == "__main__":
    string = "2314"
    # string = "345"
    pattern = re.compile('^[1234]+$')
    check(string, pattern)
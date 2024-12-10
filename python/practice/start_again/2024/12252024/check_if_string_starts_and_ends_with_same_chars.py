#   https://www.geeksforgeeks.org/python-check-whether-a-string-starts-and-ends-with-the-same-character-or-not-using-regular-expression/

import re

def CheckStartandEnd(s):
    # Single character string: '^[a-z]$'
    # Multiple character string: '^([a-z]).*\1$'
    regex = r'^[a-z]$|^([a-z]).*\1$'
    if re.search(regex, s):
        print ("Valid")
    else:
        print ("Not Valid")


if __name__ == "__main__":
    s = "abba"
    s1 = "a"
    s2 = "abcd"
    s3 = "a xxx yyyy zzzz aaaa"
    CheckStartandEnd(s)
    CheckStartandEnd(s1)
    CheckStartandEnd(s2)
    CheckStartandEnd(s3)

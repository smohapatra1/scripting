#   https://www.geeksforgeeks.org/python-regex-to-find-sequences-of-one-upper-case-letter-followed-by-lower-case-letters/

import re 

def UpperCase(s):
    regex = '[A-Z][a-z]+'
    if re.search(regex, s):
        print ("Valid")
    else:
        print ("Invalid")

if __name__ == "__main__":
    s = "Geeks"
    s1 = 'geeAkAA55of55gee4ksabc3Ar2x'
    s2 = 'geeksforgeeks'
    UpperCase(s)
    UpperCase(s1)
    UpperCase(s2)
#   https://www.geeksforgeeks.org/name-validation-using-ignorecase-in-python-regex/

import re 

def IgnoreCase(s):
    res1 = re.compile(r'^(Mr\.|Mrs\.|Ms\.) ([a-z]+)( [a-z]+)*( [a-z]+)*$', re.IGNORECASE)
    res = res1.search(s)
    if res:
        print ("Valid")
    else:
        print ("Invalid")

if __name__ == "__main__":
    s = "Mr. Albus Severus Potter"
    s1 = 'Lily and Mr. Harry Potter'
    s2 = 'Mr. Cedric'
    s3 = 'Mr. sirius black'
    IgnoreCase(s)
    IgnoreCase(s1)
    IgnoreCase(s2)
    IgnoreCase(s3)
    
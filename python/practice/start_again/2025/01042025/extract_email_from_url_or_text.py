#   https://www.geeksforgeeks.org/python-program-extract-email-id-url-text-file/

import re

def CheckEmail(s):
    x = re.findall('\S+@\S+', s)
    return x


if __name__ == "__main__":
    s = "Hello"
    s1 = "This is Geeksforgeeks"
    s2 = "review-team@geeksforgeeks.org"
    s3 = "review-team@geeksforgeeks.org"
    s4 = "GfG is a portal for geeks"
    s5 = "feedback@geeksforgeeks.org"
    s6 = "careers@geeksforgeeks.org"
    print (CheckEmail(s))
    print (CheckEmail(s1))
    print (CheckEmail(s2))
    print (CheckEmail(s3))
    print (CheckEmail(s4))
    print (CheckEmail(s5))
    print (CheckEmail(s6))

#   https://www.geeksforgeeks.org/python-regex-program-to-accept-string-ending-with-alphanumeric-character/

import re
def StringEndChar(s):
    regex = r'[a-zA-z0-9]$'
    if re.search(regex, s):
        print ("Number exists at the end")
    else:
        print ("Number doesn't exist at the end")

if __name__ == "__main__":
    s = "test326"
    s1 = "test@31#"
    StringEndChar(s)
    StringEndChar(s1)
#       https://www.geeksforgeeks.org/python-regex-check-whether-the-input-is-floating-point-number-or-not/

import re
def FloatingPoint(a):
    regex = '[+-]?[0-9]+\.[0-9]+'
    if re.search(regex, a):
        print ("A floating Number")
    else:
        print ("Not a floating Number")


if __name__ == "__main__":
    a = "1.20"
    b = "-2.356"
    c = "-3"
    FloatingPoint(a)
    FloatingPoint(b)
    FloatingPoint(c)
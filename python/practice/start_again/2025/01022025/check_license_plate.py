#   https://www.geeksforgeeks.org/check-if-license-plate-number-is-formatted-correctly-using-python/

import re

def Validate(s, pattern):
    regex = re.compile(pattern)
    if regex.match(s):
        print ("Match")
    print ("Don't match")


if __name__ == "__main__":
    s = "ABC123"
    s1 = "AB12 CDE"
    us_pattern = r'^[A-Z]{3}-\d{4}$'  # Pattern for 'ABC-1234'
    uk_pattern = r'^[A-Z]{2}\d{2} [A-Z]{3}$'  # Pattern for 'AB12 CDE'
    Validate(s, us_pattern)
    Validate(s1, uk_pattern)
## https://www.hackerrank.com/challenges/validating-the-phone-number/problem
#
# Validate Phone number 

import re

for _ in range(int(input())):
    s=input()
    print ("YES" if re.match(r"^[789]\d{9}$", s) else "NO")
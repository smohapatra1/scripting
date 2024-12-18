#   https://www.geeksforgeeks.org/python-regex-extract-maximum-numeric-value-string/

import re

def ExtractMxNum(s):
    regex = re.findall('\d+', s)
    nums = map(int, regex)
    print (max(nums))


if __name__ == "__main__":
    s = "100klh564abc365bg"
    ExtractMxNum(s)
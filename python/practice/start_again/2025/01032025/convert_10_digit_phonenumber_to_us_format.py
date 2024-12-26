#   https://www.geeksforgeeks.org/converting-a-10-digit-phone-number-to-us-format-using-regex-in-python/

import re

def ConvertNumber(s):
    s1 = re.sub(r'(?<!\S)(\d{3})-',r'(\1) ', s)
    print (s1)

if __name__ == "__main__":
    s = "123-456-7890"
    ConvertNumber(s)
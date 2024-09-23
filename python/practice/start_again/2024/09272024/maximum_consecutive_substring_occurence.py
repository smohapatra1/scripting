#   https://www.geeksforgeeks.org/python-maximum-consecutive-substring-occurrence/
import re

def Sub(test_str, sub_str):
    res = max(re.findall('((?:' + re.escape(sub_str) + ')*)', test_str), key=len)
    return res

if __name__ == "__main__":
    test_str = 'geeksgeeks are geeks for all geeksgeeksgeeks'
    sub_str = 'geeks'
    result = Sub(test_str, sub_str)
    print (result)

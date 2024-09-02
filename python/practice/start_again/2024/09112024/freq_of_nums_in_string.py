#   https://www.geeksforgeeks.org/python-frequency-of-numbers-in-string/

#   Import RegEx
#   Use Findall
#   Return the len of the returned values

import re  
def FreqNum(test_str):
    res = len(re.findall(r'\d+', test_str))
    return res

if __name__ == "__main__":
    test_str = "geeks4feeks is No. 1 4 geeks"
    result = FreqNum(test_str)
    print (result)
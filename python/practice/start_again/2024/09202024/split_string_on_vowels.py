#   https://www.geeksforgeeks.org/python-split-string-on-vowels/

import re
def Split(test_str):
    res = re.split('a|e|i|o|u', test_str)
    return res


if __name__ == "__main__":
    test_str = 'GFGaBste4oCS'
    result = Split(test_str)
    print (result)
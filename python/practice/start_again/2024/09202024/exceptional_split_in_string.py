#   https://www.geeksforgeeks.org/python-exceptional-split-in-string/?ref=leftbar-rightbar

import re 

def Exceptional(test_str):
    res = re.split(r', (?!\S\)|\()', test_str)
    return res


if __name__ == "__main__":
    test_str = "gfg, is, (best, for), geeks"
    result = Exceptional(test_str)
    print (result)
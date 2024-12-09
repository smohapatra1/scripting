#   https://www.geeksforgeeks.org/python-program-to-extract-strings-between-html-tags/


import re

def FindString(test_str, tag):
    print ("Original String : " + test_str)
    reg_str = "<" + tag + ">(.*?)</" + tag + ">"
    res = re.findall(reg_str, test_str)
    return res

if __name__ == "__main__":
    test_str = '<b>Gfg</b> is <b>Best</b>. I love <b>Reading CS</b> from it.'
    tag = "b"
    print (FindString(test_str, tag))
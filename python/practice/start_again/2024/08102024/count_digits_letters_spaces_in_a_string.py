#   Counting Digits, Letters, and Spaces in a String

import re

def Count_DLS(name):
    for i in name:
        dCount = re.sub("[^0-9]", "", name)
        nCount = re.sub("[^a-zA-Z]", "", name)
        sCount = re.sub("[ \n]", "", name)
    print ("Number of Digits  {}".format(len(dCount)))
    print ("Number of Numbers {}".format(len(nCount)))
    print ("Number of Spaces  {}".format(len(sCount)))

if __name__ == "__main__":
    name = 'Python is 1'
    result = Count_DLS(name)